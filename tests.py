import unittest
from supermarket_checkout import Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        """
        Set up a new Checkout instance before each test case.
        """
        self.checkout = Checkout()

    def test_empty_cart(self):
        """
        Test that the total is 0 when the cart is empty.
        """
        self.assertEqual(self.checkout.calculate_total(), 0)
        
    def test_single_item(self):
        """
        Test the total price for a single item.
        """
        self.checkout.scan("A")
        self.assertEqual(self.checkout.calculate_total(), 50)

    def test_multiple_items(self):
        """
        Test the total price for multiple items in various combinations.
        """
        test_cases = [
            ("AB", 80),
            ("CDBA", 115),
            ("AA", 100),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAA", 230),
            ("AAAAAA", 260),
            ("AAAB", 160),
            ("AAABB", 175),
            ("AAABBD", 190),
            ("DABABA", 190)
        ]

        for test_input, expected_output in test_cases:
            with self.subTest(test_input=test_input):
                for item in test_input:
                    self.checkout.scan(item)
                total = self.checkout.calculate_total()
                self.assertEqual(total, expected_output, f"Test failed for input: {test_input}")
                self.checkout.cart.clear()

    def test_items_not_in_price_list(self):
        """
        Test scanning items that are not in the price list.
        """
        self.checkout.scan("E")
        self.assertEqual(self.checkout.calculate_total(), 0)

    def test_mixed_case(self):
        """
        Test scanning items with a mix of upper and lower-case codes.
        """
        self.checkout.scan("a")
        self.assertEqual(self.checkout.calculate_total(), 0)

if __name__ == "__main__":
    unittest.main()
