```python
def double_the_difference(lst):
    odd = [x for x in lst if x % 2 != 0 and x >= 0]
    return sum(x * x for x in odd)
```
```python
import unittest

class TestDoubleDifference(unittest.TestCase):
    def test_odd_squares(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_negative_ignored(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_all_odd(self):
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_positive_integers_only(self):
        self.assertEqual(double_the_difference([1, 5, 7, 11, 3]), 176)

if __name__ == '__main__':
    unittest.main()
```

The function `double_the_difference()` uses list comprehension to filter out odd positive integers from the input list and then calculates the sum of their squares. The test suite verifies that the function behaves as expected for various input scenarios.