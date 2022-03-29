import unittest

from main import (
    right_shift,
)


class MainTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(right_shift("A 2"), "C")  # add assertion here

    def test_wrap_around_after_Z(self):
        self.assertEqual(right_shift("Z 5"), "E")  # add assertion here

    def test_very_large_shift(self):
        self.assertEqual(right_shift("B 80"), "D")  # add assertion here


if __name__ == '__main__':
    unittest.main()
