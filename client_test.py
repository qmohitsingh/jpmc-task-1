import unittest
from client import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_get_data_point(self):
        quote = {
            'stock': 'ABC',
            'top_bid': {'price': '100'},
            'top_ask': {'price': '110'}
        }
        expected = ('ABC', 100, 110, 105.0)
        self.assertEqual(getDataPoint(quote), expected)

        quote = {
            'stock': 'DEF',
            'top_bid': {'price': '200'},
            'top_ask': {'price': '220'}
        }
        expected = ('DEF', 200, 220, 210.0)
        self.assertEqual(getDataPoint(quote), expected)

    def test_get_ratio(self):
        # Test with positive numbers
        self.assertEqual(getRatio(1, 2), 0.5)
        self.assertEqual(getRatio(2, 1), 2.0)
        self.assertEqual(getRatio(4, 2), 2.0)

        # Test with negative numbers
        self.assertEqual(getRatio(-1, -2), 0.5)
        self.assertEqual(getRatio(-2, -1), 2.0)
        self.assertEqual(getRatio(-4, -2), 2.0)

        # Test with mixed signs
        self.assertEqual(getRatio(-1, 2), -0.5)
        self.assertEqual(getRatio(1, -2), -0.5)
        self.assertEqual(getRatio(-2, 1), -2.0)
        self.assertEqual(getRatio(2, -1), -2.0)

        # Test with 0
        self.assertEqual(getRatio(0, 2), 0.0)
        self.assertEqual(getRatio(2, 0), None)
        self.assertEqual(getRatio(0, 0), None)


if __name__ == '__main__':
    unittest.main()
