import unittest
from client3 import getDataPoint
from client3 import getRatio
class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes: self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes: self.assertEqual(getDataPoint(quote), (
    quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """
class TestGetRatio(unittest.TestCase):
    def test_valid_ratio(self):
        price_a = 10
        price_b = 5
        # Test for valid ratio when price_b is not zero
        self.assertAlmostEqual(getRatio(price_a, price_b),2) # 10/5 = 2

    def test_zero_denominator(self):
        price_a = 10
        price_b = 0
        # Test for handling zero denominator
        self.assertIsNone(getRatio(price_a, price_b))  # Expecting None when denominator is zero

    def test_zero_numerator(self):
        price_a = 0
        price_b = 5
        # Test for when numerator is zero
        self.assertEqual(getRatio(price_a, price_b),0) # 0/5 = 0

    def test_both_zero(self):
        price_a = 0
        price_b = 0
        # Test for when both numerator and denominator are zero
        self.assertIsNone(getRatio(price_a, price_b))  # Expecting None when both numerator and denominator are zero




if __name__ == '__main__':
    unittest.main()
