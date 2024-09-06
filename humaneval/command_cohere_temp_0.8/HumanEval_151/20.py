```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 == 1 and x >= 0)
    return int(odd_squares)
```
```python
import unittest

class TestDoubleTheDifference(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_example2(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_example3(self):
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_example4(self):
        self.assertEqual(double_the_difference([0]), 0)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()
```

The function `double_the_difference` works as follows:
1. It uses a list comprehension to iterate over each number in the input `nums` list.
2. For each number, it checks two conditions:
    - Whether the number is odd using the modulo operator `% 2 == 1`.
    - Whether the number is greater than or equal to zero `x >= 0`.
3. If both conditions are True, the number is included in the sum, squared, and the result is the sum of odd positive integers squared.
4. The function returns 0 if the input list is empty.
5. The test suite includes tests for the example scenarios provided in the problem statement and one additional test for an empty input list.

This code will run the moment you upload it to a Python environment and can be adjusted to run with any testing framework like `pytest` or `unittest`.