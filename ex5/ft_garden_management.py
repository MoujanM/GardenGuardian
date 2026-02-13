
class GardenManager:

    @staticmethod
    def add_plants(plant: str) -> None:
        err_msg = "Plant name cannot be empty!"
        if plant == "":
            raise GardenError(err_msg)
        print(f'Added {plant} successfully')

    @staticmethod
    def water_plants(plant_list: list) -> None:
        print("Opening watering system")
        err_msg = "Error: Cannot water None - invalid plant!"
        for plant in plant_list:
            try:
                print(f"Watering {plant} - success")  
                if plant is None:
                    raise ValueError(err_msg)
            except ValueError as e:
                print(f'{e}')
            finally:
                print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
        else:
            print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: str) -> None:
        message = f"The {plant} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, water: str) -> None:
        message = "Not enough water in the tank!"
        super().__init__(message)

def test_garden_management():
    print("=== Garden Management System ===", end='\n\n')
    plant_list = ["tomato", "lettuce", ""]
    print("Adding plants to garden...")
    try:
        for plant in plant_list:
            GardenManager.add_plants(plant)
    except ValueError as e:
        print(f"Error adding plant: {e}")
    print()
    print("Watering plants...")
    GardenManager.water_plants(["tomato", "lettuce"])
    print()
    print("Checking plant health...")
    health_check = [
        ("tomato", 5, 8),
        ("lettuce", 15, 7)
    ]
    for plant in health_check:
        try:
            GardenManager.check_plant_health(*plant)
        except ValueError as e:
            print(f"Error checking {plant[0]}: {e}")
    print()
    print("Testing error recovery...")


    

if __name__ == "__main__":
    test_garden_management()