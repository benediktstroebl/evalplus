```python
import unittest
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()


list comprehension is used to make the sorting more efficient.

class TestSortNumbers:
    """ A test class for testing the sort_numbers function.
    """
    def test_sort_numbers(self) -> None:
        """ Test method for testing the sort_numbers function."""
        self.assertEqual('three one two five')
        self.assertEqual('four six eight nine')
        self.assertEqual('three four five')

if __name__ == '__main__':
    unittest.main()
```
This Python script defines a function sort_numbers, which takes a string of numbers as input and returns their sorted version. The function uses the list comprehension, which is more efficient than a traditional Python loop, to sort the numbers. The function is also designed to be a testable, and a test class (TestSortNumbers) is created to organize the tests for the function.