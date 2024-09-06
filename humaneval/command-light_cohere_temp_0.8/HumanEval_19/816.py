```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ', numbers)
    use the sorted(numbers)
    """

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual("three one five")
        self.assertEqual("zero one two")
        self.assertEqual("two three four")
        self.assertEqual("five six seven")
        self.assertEqual("eight nine")
        def test_empty_input(self):
        self.assertEqual(None)
        self.assertEqual("")
def test_valid_input(self):
        self.assertEqual("three one five")

if __name__ == "__main__":
    unittest.main()
```