class Car:
    pass

    def __init__(self, register_number, max_speed, current_speed = 0, travelled_distance = 0):
        self.register_number = register_number
        self.max_speed = max_speed

new_car = Car ("ABC-123 ", 142)
print(f" Tä auton rekisteritunnus on: {new_car.register_number}\n Huippunopeus on: {new_car.max_speed}km/h.")
