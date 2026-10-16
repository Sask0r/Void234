import unittest

from shop import calculate_total


class TestCalculateTotal(unittest.TestCase):

    def test_order_without_discount(self):
        result = calculate_total(100, 2, 0)
        self.assertEqual(result, 200)

    def test_order_with_discount(self):
        result = calculate_total(100, 2, 10)
        self.assertEqual(result, 180)

    def test_zero_price_allowed(self):
        result = calculate_total(0, 5, 0)
        self.assertEqual(result, 0)

    def test_max_discount_allowed(self):
        result = calculate_total(200, 1, 50)
        self.assertEqual(result, 100)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_total(-100, 1, 0)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            calculate_total(100, 0, 0)

    def test_discount_above_limit(self):
        with self.assertRaises(ValueError):
            calculate_total(100, 1, 51)


if __name__ == "__main__":
    unittest.main()