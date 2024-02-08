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

if __name__ == "__main__":
    unittest.main()
