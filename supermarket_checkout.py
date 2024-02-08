class Checkout:
    """
    A class representing a checkout system for a supermarket.

    Attributes:
        prices (dict): A dictionary mapping item codes to their respective prices.
        special_offers (dict): A dictionary mapping item codes to special offer details.
        cart (dict): A dictionary representing the items scanned by the customer and their quantities.
    """

    def __init__(self):
        """
        Initializes a new instance of the Checkout class.

        The checkout system is initialized with default prices, special offers, and an empty cart.
        """
        self.prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.special_offers = {'A': (3, 130), 'B': (2, 45)}
        self.cart = {}

    def scan(self, item):
        """
        Adds an item to the cart or increments its quantity if it already exists.

        Args:
            item (str): The code representing the item to be scanned.
        """
        if item not in self.cart:
            self.cart[item] = 1
        else:
            self.cart[item] += 1

    def scan(self, item):
        """
        Adds an item to the cart or increments its quantity if it already exists.

        Args:
            item (str): The code representing the item to be scanned.
        """
        if item in self.prices:
            if item not in self.cart:
                self.cart[item] = 1
            else:
                self.cart[item] += 1
        else:
            raise ValueError(f"Item '{item}' not found in the price list.")

    def calculate_total(self):
        """
        Calculates the total price of the items in the cart, considering special offers.

        Returns:
            int: The total price of the items in the cart.
        """
        total_price = 0
        for item, quantity in self.cart.items():
            if item in self.special_offers:
                special_quantity, special_price = self.special_offers[item]
                special_offer_count = quantity // special_quantity
                remaining_count = quantity % special_quantity
                total_price += special_offer_count * special_price + remaining_count * self.prices[item]
            else:
                total_price += quantity * self.prices[item]
        return total_price

