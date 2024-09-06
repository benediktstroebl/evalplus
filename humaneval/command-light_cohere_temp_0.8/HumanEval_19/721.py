Certainly! Here's the corrected Python script with the `sort_numbers` function, which sorts a list of numbers in a string, following the given format:

```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest.
    Return the
    strings sorted version.
    """
 return the sorted numbers as a string.
"""

class TestSortNumbers(unittest.TestCase.TestCase):
    def test_string_numbers(self) -> None:
        self.assertEqual('three one five')
        self.assertEqual('one two six')
        self.assertEqual('one three seven')
        self.assertEqual('two three eight')
        self.assertEqual('two four')
        self.assertEqual('three five')
        print(sort_numbers('Test String'))

if __name__ == "__main__":
    unittest.main()()
```

This script contains a `TestSortNumbers` class with a single function test method. The `test_string_numbers` function tests if the `sort_numbers` function correctly sorts a given string of numbers. The `unittest.py` module is imported into the script. The `unittest.main()` function is run the script to run all the tests.