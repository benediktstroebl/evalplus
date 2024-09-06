```python
import unittest
from typing import List


def sort_numbers(numbers: str) -> str:
    return numbers.valid()


class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self) -> None:
        self.assertEqual("three one five")
        self.assertEqual("one two four")
        self.assertEqual("two three five")
        self.assertEqual("zero seven")
        self.assertEqual("five eight")
        self.assertEqual("six seven")
        self.assertEqual("eight nine")
        self.assertEqual("nine")


if __name__ == "__main__":
    unittest.main()
```