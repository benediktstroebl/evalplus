```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(). ' three two five'

    numbers = [int(n) for n in numbers.
    numbers.sort()
    goal = numbers
   
    return ' '.join(numbers)

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual('three one five')
        self.assertEqual('one three six')
        assert sort_numbers('three one five') == 'one three five'
        self.assertEqual('one three eight')
        self.assertEqual('one three seven')
        assert sort_numbers('one three eight') == 'one three seven'
        self.assertEqual('two three eight')
        self.assertEqual('two three six')
        assert sort_numbers('two three six') == 'two three four'

if __name__ == '__main__':
    unittest.main()
```