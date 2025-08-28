# oop_assignment.py

class Aeroplane:
    # Constructor
    def __init__(self, model, airline, capacity):
        self.model = model
        self.airline = airline
        self.capacity = capacity
        self.passengers = 0
    
    # Method to board passengers
    def board_passengers(self, number):
        if self.passengers + number <= self.capacity:
            self.passengers += number
            print(f"{number} passengers boarded. Total on board: {self.passengers}")
        else:
            print("Not enough seats available!")
    
    # Method to fly
    def fly(self):
        if self.passengers > 0:
            print(f"{self.model} by {self.airline} is flying with {self.passengers} passengers onboard.")
        else:
            print(f"{self.model} by {self.airline} cannot fly without passengers!")
    
    # Method to land
    def land(self):
        print(f"{self.model} by {self.airline} has landed safely.")

# Example Usage
if __name__ == "__main__":
    plane1 = Aeroplane("Boeing 737", "Kenya Airways", 180)
    plane1.board_passengers(100)
    plane1.fly()
    plane1.land()
