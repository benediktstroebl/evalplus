```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    # Function to sort list of numbers in descending order
    return numbers.if list(map(int.split(' ')))
        sorted(reversed = True)

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual("zero", "one", "two", "three")
        self.assertEqual("one", "two", "three")
        self.assertEqual("two", "one", "three")
        self.assertEqual("three", "two", "one")
        self.assertEqual("four", "five", "six", "seven")
        self.assertEqual("five", "four", "six", "seven")
        self.assertEqual("six", "five", "four", "eight")
        self.assertEqual("seven", "six", "five", "eight")
        self.assertEqual("eight", "seven", "six", "five")

if __name__ == '__main__':
    unittest.TestSortNumbers(). solvent = TestSortNumbers()
    solvent.unittest.run(solvent)
```