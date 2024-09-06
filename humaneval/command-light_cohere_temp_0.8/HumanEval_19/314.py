```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split().numbers = [map((i, str.toupper(i)) for i in numbers.numbers = numbers.joinsplit[numbers.map(
       sort(numbers, lambda x: ('four', 'five', 'six', 'seven', 'eight', 'nine')[int(x] - 1)]))
    return ''.join(numbers)

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual('three one five', 'zero three five', 'one zero five')
        assert sort_numbers('three one five') == 'one three five'
        assert sort_numbers('zero three five') == 'zero one five'
        assert sort_numbers('one zero five') == 'one three five'

if __name__ == "__main__":
    unittest.suite()
```