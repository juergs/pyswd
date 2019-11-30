"""STM32F1xx"""

import swd.devices.stm32 as _stm32


class Stm32f1(_stm32.Stm32):
    """STM32F1xx"""

    _NAME = "STM32F1"
    _IDCODE_REG = 0xE0042000
    _FLASH_SIZE_REG = 0x1ffff7e0
    _MCUS = [
    ]
