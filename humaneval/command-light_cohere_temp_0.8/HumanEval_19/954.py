Here's a self-contained Python function that sorts and returns a string of numbers in Markdown format, with the given test code included:
```python
import unittest
from typing import List
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    if len(numbers) == 0:
        return ""
    sort = OrderedDict()
    for num in numbers:
        sort[num] = True
    return " ".join([str(num) for num in sorted(numbers, reverse=True, key=str)])

class TestSortNumbers(unittest.TestCase.TestCase):
    def test_string_sort(test_str: str) -> None:
        expected = "one two three four five six seven eight nine"
        got = sort_numbers(test_str)
        unittest.assert(got == expected, "Test string sort failed")

if __name__ == "__main__":
    unittest.main()()
```