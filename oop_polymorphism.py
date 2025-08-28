# oop_polymorphism.py

class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Aeroplane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example Usage
if __name__ == "__main__":
    vehicles = [Aeroplane(), Car(), Boat()]

    for v in vehicles:
        v.move()
