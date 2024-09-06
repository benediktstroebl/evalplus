```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers (List[int]): list of integers, and delimiter (int): positive integer.
    Returns: A list of integers with the delimiter inserted between every two consecutive elements.
    """ Example
    `numbers` is modified to include the delimiter at the beginning and end of the list.
    Returns: List[int] with the delimiter inserted between every two consecutive elements.
    """
 modified list has the same length as the original list, and the order of elements is unchanged.
    """
example usage:
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Output: [1, 4, 2, 4, 3]

"""Unit tests"""
import unittest

class TestIntersperse(unittest.TestCase.TestCase)
 def testIntersperse(numbers: List[int], delimiter: int):
    actual = intersperse(numbers, delimiter)
    expected = [1, 4, 2, 4, 3]
    unittest.TestCase.assertEqualEqual(actual, expected, fail=False)
```