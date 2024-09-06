Here's a Python script with a self-contained function that solves the problem and includes informative tests using Python's built-in `unittest` module:
```python
import unittest

def double_the_difference(numbers):
    """
    Sum of squares of odd numbers in the list while ignoring negatives and non-integers.

    Returns 0 if the list is empty.
    """
    result = 0
    for num in numbers:
        if num % 2 != 0 and num >= 0 and isinstance(num, int):
            result += num ** 2

    return result

class TestDoubleTheDifference(unittest.TestCase):
    def test_positive_odd_numbers(self):
        """Test with a list of positive odd numbers."""
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 1 + 9 + 25 + 49)

    def test_mixed_numbers(self):
        """Test with a list of mixed numbers including positives and negatives."""
        self.assertEqual(double_the_difference([1, -3, 5, 7, -1, 2, -4]), 1 + 25 + 49 + 4)

    def test_all_positive(self):
        """Test with a list of all positive numbers."""
        self.assertEqual(double_the_difference([1, 2, 3, 4, 5]), 1 + 4 + 9 + 16 + 25)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `double_the_difference` function is defined, along with a docstring that explains its purpose and behavior.
- Four test cases are defined using Python's `unittest.TestCase` class. Each test case asserts that the function's output matches the expected result.
- The `if __name__ == '__main__':` block runs the test suite when the script is executed directly.

This way, when you run the script, the test suite is executed, and any failures or errors will be clearly indicated, helping you verify the correctness of your function.