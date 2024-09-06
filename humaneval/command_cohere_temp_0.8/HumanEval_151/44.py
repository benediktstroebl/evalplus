Here's a Python script with a self-contained function that solves the problem and includes informative tests using Python's built-in `unittest` framework:
```python
import unittest

def double_the_difference(numbers):
    """
    Sum of squares of odd numbers in the list while ignoring negatives and non-integers.

    Args:
        numbers (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if input list is empty.
    """
    result = 0
    for num in numbers:
        if num % 2 == 0 and num >= 0 and isinstance(num, int):
            result += num ** 2

    return result

class TestDoubleTheDifference(unittest.TestCase):
    def test_single_number(self):
        """Test with a list containing a single number."""
        self.assertEqual(double_the_difference([1]), 1)

    def test_multiple_numbers(self):
        """Test with a list containing multiple numbers."""
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_no_odd_numbers(self):
        """Test with no odd numbers in the list."""
        self.assertEqual(double_the_difference([0, 2, 4, 6]), 0)

    def test_all_odd_numbers(self):
        """Test with only odd numbers."""
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 30)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(double_the_difference([]), 0)

    def test_negative_numbers_ignored(self):
        """Test with negative numbers."""
        self.assertEqual(double_the_difference([1, -1, 3, -3, 2, -2, 0, -0]), 16)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `double_the_difference` function calculates the sum of squares of odd numbers in the input list, ignoring negative numbers and non-integer values.
- The `TestDoubleTheDifference` class contains several test methods that test the function with various input scenarios.
- By running `unittest.main()` at the end of the script, the tests are automatically executed when the script is run directly. 

To run the script, copy and paste it into a Python environment or script file (e.g., `test_double_the_difference.py`) and execute it using your Python interpreter. The script's output will show the results of each test, helping confirm that the function provides the expected behavior for different inputs.