import unittest
from HW01 import classify_triangle
import math


class TestHW01(unittest.TestCase):

    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(3, 14, 5), "Not a Triangle!")
        self.assertEqual(classify_triangle(0, 11, 5), "Not a Triangle!")
        self.assertEqual(classify_triangle(7, 7, 7), "Equilateral Triangle")
        self.assertEqual(classify_triangle(16, 16, 16), "Equilateral Triangle")
        self.assertEqual(classify_triangle(9, 4, 9), "Isosceles Triangle")
        self.assertEqual(classify_triangle(9, 14, 14), "Isosceles Triangle")
        self.assertEqual(classify_triangle(10, 5 * math.sqrt(2), 5 * math.sqrt(2)), "Isosceles and Right Triangle")
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(12, 5, 13), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(9, 8, 7), "Scalene Triangle")
        self.assertEqual(classify_triangle(13, 7, 14), "Scalene Triangle")


if __name__ == '__main__':
    unittest.main()
