```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers.
    return f'numbers of `{:trange(len(numbers), reverse=True)}`

class TestSortNumbers(unittest.TestCase):
    def test_sorted_numbers(self):
        self.assertEqual(sort_numbers('three one five'))
        self.assertEqual(sort_numbers('zero two three'))
        self.assertEqual(sort_numbers('six seven eight nine'))
        self.assertEqual(sort_numbers('Nine eight seven six'))
```

The above script defines a function `sort_numbers` that takes a string of numbers and returns a sorted version of that string. The function uses the range and `reverse=True` to sort the numbers from smallest to largest. The `TestSortNumbers` class contains several test methods that test the `sort_numbers` function with various input strings.