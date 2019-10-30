"""Bitfield manipulation class"""


class BitfieldException(Exception):
    """Custom exception for bitfield"""


class BitfieldRegisterValueNotExist(BitfieldException):
    """Raised if invalidated cache has been accessed"""


class BitfieldCacheIsNotValid(BitfieldException):
    """Raised if invalidated cache has been accessed"""


class _Field:
    """Bits in register"""

    def __init__(self, reg_offset, reg_bits, bits, names=None):
        self._offset = reg_offset
        self._reg_bits = reg_bits
        self._mask = 2 ** reg_bits - 1
        self._mask_off = self._mask << self._offset
        self._mask_off_inv = (2 ** bits - 1) ^ self._mask_off
        self._val_name = {}
        self._name_val = {}
        if names:
            for val, name in names:
                self._val_name[val] = name
                self._name_val[name] = val

    def _to_name(self, val, default_val=False):
        return self._val_name.get(val, val if default_val else None)

    def _to_val(self, val):
        if isinstance(val, int):
            return val
        if isinstance(val, bool):
            return int(val)
        if isinstance(val, str):
            if val in self._name_val:
                return self._name_val[val]
        raise BitfieldRegisterValueNotExist()

    def is_name(self, val):
        """Test if named value exists"""
        return val in self._name_val

    def get(self, raw):
        """Get value from bitfield"""
        return (raw >> self._offset) & self._mask

    def get_named(self, raw, default_val=False):
        """Get value from bitfield"""
        return self._to_name((raw >> self._offset) & self._mask, default_val)

    def get_bits(self, val):
        """Get bits value"""
        return (self._to_val(val) & self._mask) << self._offset

    def update(self, raw, val):
        """Update value into bitfield"""
        return (raw & self._mask_off_inv) | self.get_bits(val)

    def hex_val(self, raw):
        """Return string representation of value"""
        return f"0x{self.get(raw):0{(self._reg_bits + 3) // 4}x}"


class _Bitfield:
    """Bits representation of register"""

    def __init__(self, description, bits):
        offset = 0
        self._reg_bits = {}
        for reg_descr in description:
            reg = reg_descr[0]
            reg_bits = reg_descr[1]
            names = None
            if reg is not None:
                if len(reg_descr) > 2:
                    names = reg_descr[2]
                self._reg_bits[reg] = _Field(offset, reg_bits, bits, names)
            offset += reg_bits
        if offset != bits:
            raise BitfieldException(
                "Invalid number of bits in Bitfield (%d expected is %s)" % (
                    offset, bits))

    def get_registers(self):
        """Return list of all registers"""
        return self._reg_bits.keys()

    def get_bits(self, values):
        """Get bits value for one register"""
        value = 0
        for reg, val in values.items():
            value |= self._reg_bits[reg].get_bits(val)
        return value


class Bitfield(_Bitfield):
    """Bitfield storage"""

    def __init__(self, description, bits=32, raw=0):
        super().__init__(description, bits)
        self._raw = raw

    @property
    def raw(self):
        """Property to read raw value"""
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Property to set raw value"""
        self._raw = raw

    def get(self, reg):
        """Get register value"""
        return self._reg_bits[reg].get(self._raw)

    def hex_val(self, reg):
        """return readable value of bits"""
        return self._reg_bits[reg].hex_val(self._raw)

    def get_named(self, reg, default_val=False):
        """Get register named value"""
        return self._reg_bits[reg].get_named(self._raw, default_val)

    def set(self, reg, val):
        """Set register value"""
        self._raw = self._reg_bits[reg].update(self._raw, val)


class BitfieldMem(_Bitfield):
    """Memory mapped bitfield storage"""

    _NAME = None
    _REGISTERS = None
    _BITS = 32
    _ADDRESS = None

    def __init__(self, mem_drv, address=None):
        if self._REGISTERS is None:
            raise BitfieldException("_REGISTERS is not defined")
        self._address = self._ADDRESS
        if address is not None:
            self._address = address
        if self._address is None:
            raise BitfieldException("address is not set")
        super().__init__(self._REGISTERS, self._BITS)
        self._mem_drv = mem_drv
        self._cached = Bitfield(self._REGISTERS, self._BITS, None)

    @property
    def address(self):
        return self._address

    @property
    def raw(self):
        """Property to read raw value"""
        if self._address % 4 or self._BITS != 32:
            data = self._mem_drv.read_mem(self._address, self._BITS // 8)
            return int.from_bytes(data, byteorder='little')
        return self._mem_drv.get_mem32(self._address)

    @raw.setter
    def raw(self, raw):
        """Property to set raw value"""
        if self._address % 4:
            data = raw.to_bytes(self._BITS // 8, byteorder='little')
            self._mem_drv.write_mem(self._address, data)
        else:
            self._mem_drv.set_mem32(self._address, raw)

    @property
    def cached(self):
        """Access cached bitfield register or load current value"""
        if self._cached.raw is None:
            self._cached.raw = self.raw
        return self._cached

    @cached.setter
    def cached(self, raw):
        """Access cached bitfield register"""
        self._cached.raw = raw

    def discard_cache(self):
        """Discard content of cache"""
        self._cached.raw = None

    def write_cache(self):
        """Write cache"""
        if self._cached.raw is None:
            raise BitfieldCacheIsNotValid()
        self.raw = self._cached.raw

    def get(self, reg):
        """Get register value"""
        return self._reg_bits[reg].get(self.raw)

    def hex_val(self, reg):
        """return readable value of bits"""
        return self._reg_bits[reg].hex_val(self.raw)

    def get_named(self, reg, default_val=False):
        """Get register named value"""
        return self._reg_bits[reg].get_named(self.raw, default_val)

    def set(self, reg, val):
        """Set register value"""
        self.raw = self._reg_bits[reg].update(self.raw, val)

    def set_bits(self, values):
        """Get bits value for one register"""
        self.raw = self.get_bits(values)

    def get_name(self):
        """Get register name"""
        return self._NAME

    @property
    def bits(self):
        """return total number of bits in register"""
        return self._BITS
