```python
import unittest
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return f"{0{3}{4}{5}{6}{7}{8}{9}"[::-1].format(*sorted(numbers))]

class TestSortNumbers(unittest.TestCase):
    def test_normal_sort(self):
        self.assertEqual('three one five')
        self.assertEqual('four six eight')
        self.assertEqual('five three six seven eight')
        self.assertEqual('six seven eight nine')
        self.assertEqual('zero one two three four five six seven eight nine')

if __name__ == "__main__":
    unittest.suite.main()
```
```