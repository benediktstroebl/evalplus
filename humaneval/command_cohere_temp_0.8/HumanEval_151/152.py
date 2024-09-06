Here's a Python script with a self-contained function that solves the problem and includes informative tests using Python's `unittest` framework:
```python
import unittest

def double_the_difference(numbers):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    odd_numbers = [num for num in numbers if num % 2 != 0 and num >= 0]
    return sum(num ** 2 for num in odd_numbers)

class TestDoubleTheDifference(unittest.TestCase):
    def test_single_odd_number(self):
        """One odd number should return its square."""
        self.assertEqual(double_the_difference([1]), 1)

    def test_multiple_odd_numbers(self):
        """Multiple odd numbers should return their sum of squares."""
        self.assertEqual(double_the_difference([1, 3, 5]), 1 + 9 + 25)

    def test_no_odd_numbers(self):
        """No odd numbers should return 0."""
        self.assertEqual(double_the_difference([0, 2, -4, 6]), 0)

    def test_empty_list(self):
        """An empty list should return 0."""
        self.assertEqual(double_the_difference([]), 0)

    def test_negative_numbers_ignored(self):
        """Negative numbers should not affect the result."""
        self.assertEqual(double_the_difference([1, -2, 5, -1]), 1 + 25)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `unittest` module is used to define a test class `TestDoubleTheDifference` with individual test methods.
- Each test method checks a specific scenario and uses `self.assertEqual()` to verify if the actual result matches the expected output.
- The `if __name__ == '__main__':` block runs the tests when the script is executed directly.

To run the tests, simply execute the script. If all tests pass, it will indicate so by printing `OK`, and if any test fails, it will show the specific assertion that failed.