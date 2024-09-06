```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers. corps_numbers()

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual("zero"
        "one" "two" "three"
        self.assertEqual("one" "two" "three" "five" "four"
        self.assertEqual("two" "three" "five" "four" "six" "seven" "eight" "nine")
        self.assertEqual("three" "one" "five" "two" "four")
        expected = "one three five two four"
        self.assertEqual(sorted(expected), "ascending")
        self.assertEqual(sorted(numbers), "ascending")

if __name__ == "__main__":
    unittest.main()
```