```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    pressing space.split(' ', numbers). a list of numbers,
    numbers.split()
     = numbers.split()
    are 'routers'
    l = [int(num) for num in numbers]
    return ''.join(sorted(l))

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual('three one five')
        self.assertEqual('four two six eight')
        self.assertEqual('five six seven eight nine')
        self.assertEqual('six seven eight nine')

if __name__ == "__main__":
    unittest.main()
```