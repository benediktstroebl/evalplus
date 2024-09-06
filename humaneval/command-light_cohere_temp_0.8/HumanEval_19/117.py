```python
import unittest
from typing import List


class NumberSortingFunctionTest:

class Numbers = List[int]


class NumberSortingFunction = lambda s: s.sort_numbers(s)


class sort_numbers(numbers: Numbers) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return Numbers(numbers).sorting_function.reverse = lambda s: s.sorting_function.reverse()
   Dry run with the exception, so we can do it!
    """

class NumberSortingFunctionTest(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers, ['three', 'one', 'five'])
        self.assertEqual(sort_numbers, ['1', '3', '5'])
        self.assertEqual(sort_numbers, ['5', '3', '1'])
        self.assertEqual(sort_numbers, ['0', '5', '7'])
        self.assertEqual(sort_numbers, ['7', '5', '3'])
        self.assertEqual(sort_numbers, ['9', '8', '7'])

    def test_reverse(self):
        self.assertEqual(sort_numbers, ['zero', 'one', 'two'])
        self.assertEqual(sort_numbers, ['1', '2', '3'])
        self.assertEqual(sort_numbers, ['2', '1', '3'])
        self.assertEqual(sort_numbers, ['three', 'four', 'five'])


if __name__ == '__main__':
    unittest.main()
```