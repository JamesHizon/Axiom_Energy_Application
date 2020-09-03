import unittest
from Axiom_Cover_Letter_Test import roman_to_arabic, profit_max, eulers_formula # Import functions to test

class MyTestCases(unittest.TestCase):

    def test_roman_arabic_convert(self):

        test_MDCCLXXVI = roman_to_arabic("MDCCLXXVI")
        self.assertEqual(test_MDCCLXXVI, 1776)
        print("MDCCLXXVI has been properly converted into : " + str(test_MDCCLXXVI))

    def test_max_profit_values_2a(self):

        test_1_profit = profit_max(X = 240, Y = 320, P1 =  40, 𝑃2= 30, H1 = 2, H2 = 1)
        self.assertEqual(test_1_profit[0], 80.0)
        self.assertEqual(test_1_profit[1], 160.0)
        self.assertEqual(test_1_profit[2], 8000.0)
        print('Test 1 Acres of Corn: ' + str(test_1_profit[0]))
        print('Test 1 Acres of Oats: ' + str(test_1_profit[1]))
        print('Test 1 Profit: ' + str(test_1_profit[2]))

    # Test values from part b:
    def test_max_profit_values_2b(self):

        test_2_profit = profit_max(X = 300, Y = 380, P1 =  70, 𝑃2= 45, H1 = 3, H2 = 1)
        self.assertEqual(test_2_profit[0], 40.0)
        self.assertEqual(test_2_profit[1], 260.0)
        self.assertEqual(test_2_profit[2], 14500.0)
        print('Test 2 Acres of Corn: ' + str(test_2_profit[0]))
        print('Test 2 Acres of Oats: ' + str(test_2_profit[1]))
        print('Test 2 Profit: ' + str(test_2_profit[2]))

    # Test values from part c:
    def test_max_profit_values_2c(self):

        test_3_profit = profit_max(X = 180, Y = 420, P1 =  65, 𝑃2= 55, H1 = 3, H2 = 2)
        self.assertEqual(test_3_profit[0], 60.0)
        self.assertEqual(test_3_profit[1], 120.0)
        self.assertEqual(test_3_profit[2], 10500.0)
        print('Test 3 Acres of Corn: ' + str(test_3_profit[0]))
        print('Test 3 Acres of Oats: ' + str(test_3_profit[1]))
        print('Test 3 Profit: ' + str(test_3_profit[2]))

    def test_eulers_formula(self):

        test_ef = eulers_formula(x0 = 1, x1 = 4, f_x0 = 8, h = 0.25)
        self.assertEqual(test_ef[1], 8.0)
        print('The approximate value of f(x1) given x1 = 4 is: ' + str(test_ef[1]))

if __name__ == '__main__':
    unittest.main()
