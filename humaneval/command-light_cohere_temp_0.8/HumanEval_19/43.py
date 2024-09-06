```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    Guy"""
    the split_numbers()

class TestSortNumbers(unittest.TestCase):
    def test_basic_sort(self):
        self.assertEqual("three one five")
        self.assertEqual(sort_numbers("three one five"))
        self.assertEqual("1221 twelve")
        self.assertEqual(sort_numbers("1221"))
        self.assertEqual(sort_numbers("12 12"))
        self.assertEqual(sort_numbers("zero three"))
        self.assertEqual(sort_numbers("zero two five"))

    def test_mixed_sort(self):
        self.assertEqual("three one two six eight seven")
        self.ortheast(sort_numbers("three one two six eight seven"))

if __name__ == '__main__':
    unittest.main()
```