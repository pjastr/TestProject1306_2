class Car:
    """Klasa opisująca samochody."""

    def __init__(self, serial, capacity):
        self.serial = serial
        self.capacity = capacity

    def load(self, good: int) -> None:
        """Metoda ładująca."""
        pass

    def __str__(self):
        return f"Car: {self.serial},{self.capacity}"


class PassengerCar(Car):

    def load(self, passengers):
        self.capacity += passengers

    def __str__(self):
        return f"PassengerCar: {self.serial},{self.capacity}"


class FreightCar(Car):
    def __init__(self, serial):
        self.goods = []
        super().__init__(serial, 0)

    def load(self, good):
        self.capacity += 1
        self.goods.append(good)

    def __str__(self):
        return f"FreightCar: {self.serial},{self.capacity},{self.goods}"
