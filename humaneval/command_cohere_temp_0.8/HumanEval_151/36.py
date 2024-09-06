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
        if isinstance(num, int) and num % 2 != 0 and num >= 0:
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
        self.assertEqual(double_the_difference([-1, -2, -5]), 0)

    def test_non_integer_values(self):
        self.assertEqual(double_the_difference([1.5, 2, 3]), 0)

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `double_the_difference` function accepts a list of numbers, squares odd integers while ignoring non-integer and negative numbers, and returns the sum of these squares.
- The `test_double_the_difference` class includes several test methods that cover different scenarios such as single numbers, negatives, empty list, and non-integer values.
- By using `unittest.main()` inside the script's main body, all the test cases are automatically run when the script is executed directly. 

To run the script, save it as a `.py` file and execute it via the command line or terminal. The built-in `unittest` module will run all the test cases and report the results, making it easy to verify the function's behavior matches the expected output.