class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def get_info(self):
        return f"{self.brand} {self.model} costs ${self.price}"
    
    def make_call(self, number):
        return f"Calling {number} from {self.model}"

class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, refresh_rate):
        super().__init__(brand, model, price)
        self.refresh_rate = refresh_rate
    
    def get_info(self):
        return f"{self.brand} {self.model} with {self.refresh_rate}Hz display costs ${self.price}"

class Vehicle:
    def move(self):
        return "This vehicle moves in a unique way"

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

phone = Smartphone("Apple", "iPhone 15", 999)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 1200, 144)
car = Car()
plane = Plane()
boat = Boat()

print(phone.get_info())
print(phone.make_call("+123456789"))
print(gaming_phone.get_info())
print(car.move())
print(plane.move())
print(boat.move())
