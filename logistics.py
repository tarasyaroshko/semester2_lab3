"""
Logistic System Module
"""
last_order = 16326465


class Item:
    """
    Item class
    """

    def __init__(self, name, price) -> None:
        """
        Init function
        >>> item = Item('shower', 500)
        >>> item.name
        'shower'
        >>> item.price
        500
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Represent object when printing.
        >>> item = Item('shower', 500)
        >>> str(item)
        'Item shower has a price of 500 UAH.'
        """
        return f"Item {self.name} has a price of {self.price} UAH."


class Vehicle:
    """
    Vehicle class
    """

    def __init__(self, vehicleNo, isAvailable=True) -> None:
        """
        Init function
        >>> truck = Vehicle(1, False)
        >>> truck.vehicleNo
        1
        >>> truck.isAvailable
        False
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Location:
    """
    Location class
    """

    def __init__(self, city, postoffice) -> None:
        """
        Init function
        >>> address = Location('New York City', 1453)
        >>> address.city
        'New York City'
        >>> address.postoffice
        1453
        """
        self.city = city
        self.postoffice = postoffice


class Order:
    """
    Order class
    """

    def __init__(self, user_name, city, postoffice, items):
        """
        Init function
        >>> items_list = [Item('shower',500), Item('bread', 17.5)]
        >>> order = Order('Oleg', 'Chornobaivka', 201, items_list)
        Your order number is 16326465.
        >>> order.user_name
        'Oleg'
        """
        global last_order
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.orderId = last_order
        last_order += 1
        self.vehicle = None

        print(f"Your order number is {self.orderId}.")

    def __str__(self):
        """
        Represent an object when printing.
        """
        return f"Order number for {self.user_name} is {self.orderId}, going to postoffice №{self.location.postoffice} in {self.location.city}"

    def calculateAmount(self):
        return sum(item.price for item in self.items)

    def assignVehicle(self, vehicle):
        self.vehicle = vehicle


class LogisticSystem:
    def __init__(self, vehicles) -> None:
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order):
        """
        Places order by assigning a vehicle.
        """
        self.orders.append(order)
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                vehicle.isAvailable = False
                order.assignVehicle(vehicle)
                return
        print("There is no available vehicle to deliver an order.")

    def trackOrder(self, other):
        """
        Tracks the order if one exists.
        """
        for order in self.orders:
            if other.orderId == order.orderId:
                if order.vehicle:
                    print(
                        f"Your order #{order.orderId} is sent to {order.location.city}. Total price: {order.calculateAmount()} UAH."
                    )
                    return
                else:
                    print(f"No such order.")
                    return


def main():
    """
    Main function
    """
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item("book", 110), Item("chupachups", 44)]
    my_order = Order(user_name="Oleg", city="Lviv", postoffice=53, items=my_items)
    logSystem.placeOrder(my_order)
    logSystem.trackOrder(my_order)
    my_items2 = [Item("flowers", 11), Item("shoes", 153), Item("helicopter", 0.33)]
    my_order2 = Order("Andrii", "Odessa", 3, my_items2)
    logSystem.placeOrder(my_order2)
    logSystem.trackOrder(my_order2)
    my_items3 = [Item("coat", 61.8), Item("shower", 5070), Item("rollers", 700)]
    my_order3 = Order("Olesya", "Kharkiv", 17, my_items3)
    logSystem.placeOrder(my_order3)
    logSystem.trackOrder(my_order3)


if __name__ == "__main__":
    main()
