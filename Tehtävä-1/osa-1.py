class Car:
    pass

    def __init__(self, register_number, max_speed, current_speed = 0, travelled_distance = 0):
        self.register_number = register_number
        self.max_speed = max_speed

    def accelerate(self, speed_change):
        if speed_change > 0:
            self.current_speed = max(self.current_speed + speed_change)
        else:
            self.current_speed = min(self.current_speed + speed_change)

new_car = Car ("ABC-123 ", 142)
print(f"Tää autoon rekisterinumero on: {new_car.register_number} \nHuippunopeus on: {new_car.max_speed} km/h.")
