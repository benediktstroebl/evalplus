Here's a Python script with a self-contained function that solves the problem and includes informative tests using Python's built-in `unittest` module:
```python
import unittest

def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list while ignoring negatives and non-integers.

    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if input list is empty.
    """
    result = 0
    for num in nums:
        if num % 2 != 0 and num >= 0 and isinstance(num, int):
            result += num ** 2

    return result

class TestDoubleTheDifference(unittest.TestCase):
    def test_single_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)

    def test_non_integer_values(self):
        self.assertEqual(double_the_difference([1.5, 2, 3.7]), 0)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `double_the_difference` function accepts a list of numbers, squares odd integers while ignoring non-integers and negatives, and returns the sum of these squares.
- The `TestDoubleTheDifference` class contains several test methods that verify the function's behavior against various test cases.
- Using `unittest.main()` facilitates running the tests when the script is executed directly.

This code encapsulates the problem solution, making it readable and reusable for anyone tackling a similar problem.