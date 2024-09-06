```python
import unittest
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.
    """ Convert to sorted numbers from smallest to largest
    >>> numbers = ['three one five', 'nine', 'eight', 'two', 'seven']
    sorted_numbers = sort_numbers(' '.join(numbers))
    return sorted_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sorted_numbers(['zero', 'two', 'three', 'four', 'five', 'six', 'seven']))
        self.assertEqual(sorted_numbers(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
        self.assertEqual(sorted_numbers([1, 3, 5, 6, 2, 7, 8, 9]))
        self.assertEqual(sorted_numbers(['zero', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']))

if __name__ == '__main__':
    unittest.main()
```