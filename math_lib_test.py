import unittest
from math_lib import add, sub, multi, div, pow2

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        result = add(55, 212)
        self.assertEqual(result, 267)

    def test_sub(self):
        result = sub(652, 237)
        self.assertEqual(result, 415)

    def test_multi(self):
        result = multi(772, 321)
        self.assertEqual(result, 247812)

    def test_div(self):
        result = div(8823, 3)
        self.assertAlmostEqual(result, 2941, places=2)

    def test_pow2(self):
        result = pow2(2, 6)
        self.assertEqual(result, 64)

        result = pow2(64, 8)
        self.assertEqual(result, 281474976710656)


if __name__ == '__main__':
    unittest.main()