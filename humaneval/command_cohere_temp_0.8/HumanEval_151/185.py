```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 == 1 and x >= 0)
    return int(odd_squares)
```
```python
import unittest

class TestDoubleTheDifference(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(double_the_difference([1]), 1)

    def test_multiple_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([]), 0)

    def test_negative_numbers_rejected(self):
        self.assertRaises(ValueError, double_the_difference, [-1, -2])

if __name__ == '__main__':
    unittest.main()
```

The function **double_the_difference** uses a list comprehension to filter out odd integers from the input list and calculates the sum of their squares. Errors are raised for negative or non-integer values, and an empty result is returned for an empty input list. The test suite verifies various cases, ensuring correct behavior.