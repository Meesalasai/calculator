import unittest

from src.calculator import add, subtract, multiply


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(10, 5)
        assert result == 15

    def test_subtract(self):
        result = subtract(10, 5)
        assert result == 5

    def test_multiply(self):
        result = multiply(10, 5)
        assert result == 50


if __name__ == '__main__':
    unittest.main()
