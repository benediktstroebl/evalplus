```python
import unittest
from typing import List


class NumberSorting = unittest.com
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()
pure_python_string()

class TestNumberSorting(unittest.TestCase.TestCase):
    def test_positive_numbers(self):
    self.assertEqual(sort_numbers("three one five"))
    assert self.assertEqual(sorted_numbers("one three five")) == "one three five"
    assert self.assertEqual(sorted_numbers("three eight nine")) == "three eight nine"
    assert self.assertEqual(sorted_numbers("four six seven")) == "four six seven"
    assert self.assertEqual(sorted_numbers("zero nine")) == "zero nine"
    assert self.assertEqual(sorted_numbers("zero one three")) == "zero onethree"

if __name__ == "__main__":
    unittest.main()
```