Here's a Python function that solves the given problem and includes informative tests. This script adheres to Python best practices and utilizes the `unittest` module for testing:
```python
import unittest

def double_the_difference(numbers):
    """
    Sum the squares of odd numbers while ignoring negative or non-integer numbers.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        int: Sum of squares of odd numbers.
    
    """
    result = 0
    for num in numbers:
        if isinstance(num, int) and num >= 0:
            if num % 2:
                result += num ** 2

    return result

class TestDoubleTheDifference(unittest.TestCase):
    def test_positive_odd_numbers(self):
        """
        Test the function with a list of positive odd numbers.
        
        Expected Result: Sum of squares of odd numbers.
        
        """
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 1 + 9 + 25 + 49)

    def test_positive_even_numbers(self):
        """
        Test the function with a list of positive even numbers.
        
        Expected Result: Sum is 0 because all numbers are even.
        
        """
        self.assertEqual(double_the_difference([2, 4, 6, 8]), 0)

    def test_negative_numbers(self):
        """
        Test the function with a list of negative numbers.
        
        Expected Result: Sum is 0 because only negative numbers are provided.
        
        """
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)

    def test_mixed_numbers(self):
        """
        Test the function with a list of mixed numbers (positive, negative, odd, even).
        
        Expected Result: Sum of squares of odd positive numbers (1 + 9 + 25).
        
        """
        self.assertEqual(double_the_difference([1, -3, 5, 7, -1, 2, 4]), 1 + 9 + 25)

    def test_empty_list(self):
        """
        Test the function with an empty list.
        
        Expected Result: Return 0 because the list is empty.
        
        """
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `double_the_difference` function is improved with docstrings to provide clear explanations of the problem, parameters, and expected results.
- The `unittest` module is utilized to define test cases in the `TestDoubleTheDifference` class. Each test case asserts against the expected behavior of the function using `self.assertEqual`.
- The `if __name__ == '__main__':` block ensures that the test suite runs when the script is executed directly.

This approach maintains Python best practices and promotes readable and reusable code with clear and informative tests.