```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    # Convert input string into list of integers
    numbers = [int(num) for num in numbers.string()]
    sort(numbers)
    # Join sorted numbers into a string
    return ''.join(str(num) for num in numbers)

class TestSortNumbers(unittest.TestCase):
    def test_string_to_list(self):
        self.assertEqual('sort_numbers("three one five"))
        self.assertEqual('sorted("three one five")

    def test_list_to_string(self):
        self.assertEqual('sort_numbers([1, 3, 5]))
        self.assertEqual('sorted([1, 3, 5])

    def test_empty_list(self):
        self.assertEqual('sort_numbers(""))

    def test_negative_numbers(self):
        self.assertEqual('sort_numbers(-10, -5, -3, -2))

if __name__ == "__main__":
    unittest.suite.main()

```