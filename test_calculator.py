# https://github.com/emferrara2006/lab11-EF-AN.git
# Partner 1: Ethan Ferrara
# Partner 2: Andres Noguera (Didn't respond to me at all)

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    #3def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 3), 9)
	self.assertEqual(multiply(-3, 3), -9)
	self.assertAlmostEqual(multiply(2.5, 2.5), 6.25)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(3, 9), 3)
	self.assertEqual(divide(-3, 9), -3)
	self.assertEqual(divide(3, -9), -3)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
		logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(2, 4), 4.472)
	self.assertAlmostEqual(hypotenuse(3, -3), 4.242)
	self.assertAlmostEqual(hypotenuse(-4, 1), 4.123)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    	with self.assertRaises(ValueError):
		square_root(-1)
	self.assertEqual(square_root(4), 2)
	self.assertAlmostEqual(square_root(5), 2.236)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
