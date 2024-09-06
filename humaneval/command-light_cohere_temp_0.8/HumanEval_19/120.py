```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
   } re.findall(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
numbers = "three one five"

class TestSortNumbers(unittest.TestCase):
    def test_single_digit_sort(self):
        self.assertEqual(self.sort_numbers("one three five"))
        assert self.assertEqual(sorted("one three five")) == "one three five"

    def test_duplicates_sort(self):
        self.assertEqual(self.sort_numbers("three six seven eight nine"))
        assert self.assertEqual(sorted("six seven eight nine")) == "six seven eight nine"

    def test_mixed_sort(self):
        self.assertEqual(self.sort_numbers("three eight five seven"))
        assert self.assertEqual(sorted("three eight five seven")) == "three eight five seven"

if __name__ == "__main__":
    unittest.TestSortNumbers(). buy = unittest.main()
```