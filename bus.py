class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        # Get the base fare from the parent class
        base_fare = super().fare()
        # Add 10% maintenance charge
        total_fare = base_fare + (0.1 * base_fare)
        return total_fare


# Create an instance of Bus with a seating capacity of 50
bus = Bus(seating_capacity=50)
print(f"The total fare for the bus ride is: INR {bus.fare()}")
