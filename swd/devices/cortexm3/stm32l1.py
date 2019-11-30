"""STM32F1xx"""

import swd.devices.memory as _mem
import swd.devices.stm32 as _stm32


class Stm32l1(_stm32.Stm32):
    """STM32L1xx"""

    _NAME = "STM32L1"
    _IDCODE_REG = 0xE0042000
    _FREQ = 32000000
    _MCUS = [
        {
            'mcu_name': 'STM32L100x6',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 32 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 4 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 2 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L100.svd',
        }, {
            'mcu_name': 'STM32L100x6-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 32 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 4 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 2 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L100.svd',
        }, {
            'mcu_name': 'STM32L100x8',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 64 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 8 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 2 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L100.svd',
        }, {
            'mcu_name': 'STM32L100x8-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 64 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 8 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 2 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L100.svd',
        }, {
            'mcu_name': 'STM32L100xB',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 128 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 10 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 2 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L100.svd',
        }, {
            'mcu_name': 'STM32L100xB-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 128 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 16 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 2 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L100.svd',
        }, {
            'mcu_name': 'STM32L100xC',
            'dev_id': 0x427,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 256 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 16 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L100.svd',
        }, {
            'mcu_name': 'STM32L151x6',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 32 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 10 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151x6-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 32 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 16 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151x8',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 64 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 10 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151x8-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 64 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151xB',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 128 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 16 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151xB-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 128 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151xC',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 256 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 8 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151xC-A',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 256 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 8 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151xD',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 384 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 48 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 12 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151xD-X',
            'dev_id': 0x437,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 384 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 80 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 16 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L151xE',
            'dev_id': 0x437,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 512 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 80 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 16 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152x6',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 32 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 10 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152x6-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 32 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 16 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152x8',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 64 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 10 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152x8-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 64 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152xB',
            'dev_id': 0x416,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 128 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 16 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152xB-A',
            'dev_id': 0x429,
            'flash_size_reg': 0x1ff8004c,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 128 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 4 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 4 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152xC',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 256 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 8 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152xC-A',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 256 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 8 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152xD',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 384 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 48 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 12 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152xD-X',
            'dev_id': 0x437,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 384 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 80 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 16 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L152xE',
            'dev_id': 0x437,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 512 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 80 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 16 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L151.svd',
        }, {
            'mcu_name': 'STM32L162xC',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 256 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 8 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L162.svd',
        }, {
            'mcu_name': 'STM32L162xC-A',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 256 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 32 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 8 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L162.svd',
        }, {
            'mcu_name': 'STM32L162xD',
            'dev_id': 0x436,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 384 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 48 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 12 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L162.svd',
        }, {
            'mcu_name': 'STM32L162xD-X',
            'dev_id': 0x437,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 384 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 80 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 16 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L162.svd',
        }, {
            'mcu_name': 'STM32L162xE',
            'dev_id': 0x437,
            'flash_size_reg': 0x1ff800cc,
            'memory': [
                {
                    'kind': 'FLASH',
                    'address': 0x08000000,
                    'size': 512 * _mem.KILO,
                    'page_size': 256,
                }, {
                    'kind': 'SRAM',
                    'address': 0x20000000,
                    'size': 80 * _mem.KILO,
                }, {
                    'kind': 'EEPROM',
                    'address': 0x08080000,
                    'size': 16 * _mem.KILO,
                }, {
                    'name': 'SYSTEM_MEMORY',
                    'kind': 'OTP',
                    'address': 0x1ff00000,
                    'size': 8 * _mem.KILO,
                }],
            'freq': 32,
            'flash_page_size': 256,
            'svd_file': 'svd/STM32L1_svd_V1.2/STM32L162.svd',
        },
    ]
