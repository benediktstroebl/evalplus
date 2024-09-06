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
    result = sum(x ** 2 for x in map(lambda x: round(x), lst))
    return result
```

The code uses a generator expression with a map function to square each number and round it to the nearest integer, then sums the resulting integers. 

To verify the functionality, you can add test cases in the following format:
```python
#test_sum_squares.py
import unittest
from sum_squares import sum_squares

class TestSumSquares(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(sum_squares([4]), 16)

    def test_multiple_numbers(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)

    def test_negative_numbers(self):
        self.assertEqual(sum_squares([-2, 2, 3]), 26)

    def test_mixed_numbers(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0, -2.4]), 29)

if __name__ == '__main__':
    unittest.main()
```

If you have any other questions on solving specific problems or need further assistance with the code, feel free to ask!