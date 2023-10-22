from enum import Enum
from datetime import date, timedelta


class PlantType(Enum):
    AIR = 1
    SUCCULENT = 2
    DWARF_UMBRELLA = 3
    BROMELIAD = 4

class Pot(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    EXTRA_LARGE = 4
    NONE = 5


DAYS_BETWEEN_WATERINGS_BY_PLANT_TYPE = {
    PlantType.AIR : 7,
    PlantType.SUCCULENT : 14,
    PlantType.DWARF_UMBRELLA : 9,
    PlantType.BROMELIAD : 10
}


class Plant():
    WINTER_MONTHS = [12, 1, 2, 3]

    def __init__(self, plant_type, plant_name, pot_size=Pot.MEDIUM,) -> None:
        self.plant_type = plant_type
        self.plant_name = plant_name
        self.pot_size = pot_size
        self.last_watered = date.today()
        self.original_days_between_waterings = DAYS_BETWEEN_WATERINGS_BY_PLANT_TYPE[self.plant_type]

        self._update_days_between_waterings()
        

    def next_watering_date(self) -> date:
        return self.last_watered + timedelta(self.days_between_waterings)

    def needs_watered(self) -> bool:
        return self.next_watering_date() <= date.today()

    def is_winter(self) -> bool:
        return date.today().month in self.WINTER_MONTHS
    
    def water_plant(self) -> None:
        self.last_watered = date.today()
        self._update_days_between_waterings()

    # helper functions
    def _update_days_between_waterings(self) -> None:
        if not self.is_winter():
            self.days_between_waterings = self.original_days_between_waterings
            return
        if self.plant_type == PlantType.SUCCULENT or self.plant_type == PlantType.BROMELIAD:
            self.days_between_waterings = self.original_days_between_waterings * 2




    