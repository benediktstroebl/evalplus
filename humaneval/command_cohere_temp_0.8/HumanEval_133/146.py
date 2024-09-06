```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: The sum of squared integers in the list.
    """
    result = 0
    for n in lst:
        rounded_n = int(n)
        result += rounded_n ** 2
    
    return result
```

The function `sum_squares` takes a list of numbers, squares each integer in the list, and returns their sum. It assumes that the list contains only single-precision floating-point numbers or integers.

To round each number in the list before squaring, the function int(n) is used, which rounds a number to the nearest integer. If n is already an integer, int(n) is equivalent to just n, thus ensuring the correctness of the function for integer-only inputs. 

The function does not explicitly separate out the input description and the examples as shown in the provided docstring, but it contains the mandatory parts and covers the functionality sufficiently to match the problem statement.

Note that the function assumes that the list contains only numeric values or integers, and it may raise a TypeError or return a NaN if a non-numeric value is encountered. 

To handle such cases and enhance the function, we can add tests and input validation:
```python
import unittest

class TestSumSquares(unittest.TestCase):

    def test_valid_inputs(self):
        # Valid inputs
        self.assertEqual(sum_squares([1, 2, 3]), 14)
        self.assertEqual(sum_squares([1, 4, 9]), 98)
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

    def test_invalid_inputs(self):
        # Invalid inputs
        self.assertRaises(TypeError, sum_squares, ['a', 'b', 'c'])
        self.assertRaises(TypeError, sum_squares, [1, 2, 'three'])
        self.assertRaises(TypeError, sum_squares, [1, 2, 3.5])
        self.assertRaises(TypeError, sum_squares, [1, 2, '42'])
        self.assertEqual(sum_squares([1, 2, None]), NaN)
        self.assertEqual(sum_squares([None, 2, 3]), NaN)
        self.assertEqual(sum_squares([1, 2, 3, None]), NaN)
``` 

To run the test suite, you can import the `unittest` module and execute the test suite using the `unittest.main()` function:
```python
import unittest

class TestSumSquares(unittest.TestCase):
    # ... Test cases ...

if __name__ == '__main__':
    unittest.main()
``` 

This way, running the script will execute the test suite, and it will output whether the tests pass or fail.