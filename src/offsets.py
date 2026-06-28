from dataclasses import dataclass

@dataclass
class Offsets:
    base_address: int = 0x2A4B498
    hp_current: int = 0x270
    hp_max: int = 0x274
    atk: int = 0x278
    def_: int = 0x27C
    magic: int = 0x280
    gold: int = 0x298
    inventory_ptr: int = 0x2B8
    battle_flag: int = 0x2F0
    timer: int = 0x308
    items_base: int = 0x2A4B588

CURRENT_OFFSETS = Offsets()
