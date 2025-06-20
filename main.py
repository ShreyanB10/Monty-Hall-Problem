import random

class Door:
    doors: list["Door"] = []
    win_count: int = 0
    simulation_count: int = 0

    def __init__(self, number: int, content: str) -> None:
        self.number = number
        self.content = content 
        Door.doors.append(self)

    @staticmethod
    def create_doors() -> None:
        Door.doors = []
        for i in range(1,4):
            Door(i, "goat")
    
    @staticmethod
    def select_door() -> int:
        first_choice: int = random.randint(1,3)
        return first_choice
        
    @staticmethod
    def pick_car_door() -> int:
        car_door: int = random.randint(1,3)
        for door in Door.doors:
            if door.number == car_door:
                Door.doors[car_door - 1].content = "car"
                break
        return car_door
    
    @staticmethod
    def find_other_door(first_choice: int, second_door: int) -> int:
        other_door: int = 0
        for door in Door.doors:
            if first_choice != door.number and second_door != door.number:
                other_door = door.number
                break
        return other_door

    @staticmethod
    def find_final_door_content(new_door: int) -> str:
        for door in Door.doors:
            if new_door == door.number:
                return door.content
        return "whole lot of air"
    
    @staticmethod
    def print_door_info():
        for door in Door.doors:
            print(f"Door {door.number}: {door.content}")

def main():
    is_running = True
    while is_running:
        try:
            repeats: int = int(input("How many simulations would you like to run? (enter 0 to exit) "))
            if repeats == 0:
                is_running = False
                break
        except ValueError:
            print(f"Error: Not a valid integer!")
            continue
        except Exception:
            print(f"Error: Something has gone wrong!")
            continue    

        switching_decision: str = input("Would you like to switch or not? (y/n) ")
        if switching_decision != "y" and switching_decision != "n":
            print("Error: Please enter y or n!")
            continue

        printing_decision: str = input("Would you like to print feedback or not? (y/n) ")
        if switching_decision != "y" and switching_decision != "n":
            print("Error: Please enter y or n!")
            continue
 
        for _ in range(repeats):
            Door.create_doors()

            car_door: int = Door.pick_car_door()
            choice: int = Door.select_door()
            opened_door: int = Door.find_other_door(choice, car_door)
            if switching_decision == "y":
                choice: int = Door.find_other_door(choice, opened_door)
            final_door_content: str = Door.find_final_door_content(choice)
            
            if final_door_content == "car":
                Door.win_count += 1
            Door.simulation_count += 1

            if printing_decision == "y":
                print()
                print(f"I selected Door {choice}.")
                print(f"Door {opened_door} contains a goat.")
                if switching_decision == "y":
                    print("Switched!")
                print(f"My door had a {final_door_content}!")
    
        print()
        print(f"You won the car {Door.win_count} out of {Door.simulation_count} times ({((Door.win_count / Door.simulation_count) * 100):.2f}%)!")            
        
if __name__ == "__main__":
    main()