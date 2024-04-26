import requests
import userinfo
import pickle
from plant import Plant, PlantType, Pot


class PlantReminder():
    def __init__(self, plants) -> None:
        self.plants = plants
        self.target = userinfo.target_phone_number


    def add_plant(self, plant) -> list:
        self.plants.append(plant)
        return self.plants
    
    def remove_plant(self, plant_name) -> list:
        self.plants = filter(lambda p: p.plant_name != plant_name, self.plants)
        return self.plants
    
    def get_message(self) -> str:
        not_watered = list(filter(lambda p: p.needs_watered(), self.plants))
        if len(not_watered) == 0:
            return 'All your plants are feeling hydrated today :)'
        
        message = ''
        for plant in not_watered:
            message += f'{plant.plant_name} needs watered today\n'
            plant.water_plant()
        
        return message

    
    def send_text(self) -> None:
        # print({ 
        #     'phone': self.target, 
        #     'message': self.get_message(), 
        #     'key': 'textbelt',
        # })

        resp = requests.post('https://textbelt.com/text', {
        'phone': self.target,
        'message': self.get_message(),
        'key': 'textbelt',
        })
        print(resp.json())

INITIAL_PLANTS = [
    Plant(PlantType.AIR, 'the little air plant fella', pot_size=Pot.NONE),
    Plant(PlantType.SUCCULENT, 'Lenny the succulent', pot_size=Pot.SMALL),
    Plant(PlantType.DWARF_UMBRELLA, 'the leafy boy', Pot.MEDIUM),
    # Plant(PlantType.BROMELIAD, 'the orange flower', Pot.MEDIUM)
]

def run() -> None:
    try:
        plant_reminder = pickle.load(open('plant_reminder.pkl', 'rb'))
    except:
        plant_reminder = PlantReminder(INITIAL_PLANTS)

    plant_reminder.send_text()
    pickle.dump(plant_reminder, open('plant_reminder.pkl', 'wb'))

run()


