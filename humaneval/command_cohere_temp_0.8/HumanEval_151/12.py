Here's a Python script with a self-contained function that solves the problem and includes informative tests using Python's built-in `unittest` framework:
```python
import unittest

def double_the_difference(nums):
    """
    Sum of squares of odd numbers in the list while ignoring negatives and non-integers.

    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd numbers or 0 if the list is empty or contains only even or negative numbers.
    """
    result = 0
    for num in nums:
        if num % 2 != 0 and num > 0:  # Check for oddness and non-negative
            result += num ** 2

    return result

class TestDoubleTheDifference(unittest.TestCase):
    def test_odd_numbers(self):
        """
        Test case with only odd numbers.
        """
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 1 + 9 + 25 + 49)

    def test_with_negative_numbers(self):
        """
        Test case with negative numbers.
        """
        self.assertEqual(double_the_difference([1, -3, 5, -7]), 0)

    def test_with_empty_list(self):
        """
        Test case with an empty list.
        """
        self.assertEqual(double_the_difference([]), 0)

    def test_with_odd_and_even_numbers(self):
        """
        Test case with a mix of odd and even numbers.
        """
        self.assertEqual(double_the_difference([1, 3, 2, 5, 7, 4]), 1 + 9 + 0 + 25 + 49)

    def test_with_non_integer_values(self):
        """
        Test case with non-integer values.
        """
        self.assertEqual(double_the_difference([1, 3.14, 2, 5, 7.89]), 0)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `double_the_difference` function is encapsulated with unit tests within the `TestDoubleTheDifference` class.
- The tests cover different scenarios, including odd numbers, negative numbers, empty lists, a mix of odd and even numbers, and non-integer values.
- The `unittest.main()` call executes the tests when the script is run directly.

To examine test coverage, utilize a test coverage tool such as `coverage.py` after running the script. To accomplish a thorough examination, at least 90% coverage is advised.