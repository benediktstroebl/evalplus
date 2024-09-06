```python
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    rounded_lst = [round(x) for x in lst]
    return sum(x * x for x in rounded_lst)
```

The function `sum_squares` serves the purpose of calculating the sum of squared integers in an input list. Before performing the summation, each list item is rounded up to the nearest integer. This is achieved through the list comprehension and the use of the `round` function.

To test this function, you can create a test file, e.g., `test_sum_squares.py`, and use the following code:
```python
import unittest
from sum_squares import sum_squares

class TestSumSquares(unittest.TestCase):
    def test_sum_squares_with_given_examples(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)
        self.assertEqual(sum_squares([1, 4, 9]), 98)
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)
        self.assertEqual(sum_squares([1, 4.2, 0]), 29)
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

if __name__ == '__main__':
    unittest.main()
```

This code will automatically run the test class TestSumSquares and verify that the `sum_squares` function produces the expected outputs for each example provided in the docstring.  Any failure to meet the expectations will result in an error, enabling thorough testing of the function's correctness.