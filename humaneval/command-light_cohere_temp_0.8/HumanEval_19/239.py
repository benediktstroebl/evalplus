```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ', numbers)
    generate list of numbers
    numbers = [int(num) for num in numbers.sort_and_count(numbers)
    numbers = [''.join(numbers) + ' ']
    return numbers[::-1]

def sort_and_count(numbers: List[int]) -> List[str]:
    """ Count the number of digits in each number, and sort the list with that count.
    numbers = sorted(numbers, key=lambda num: num)
    return numbers

class TestSortNumbers(unittest.TestCase):
    def test_string_to_list(self):
        self.assertEqual(sort_numbers('three one five'))
        assert ['one', 'three', 'five'] == numbers

    def test_list_to_list(self):
        self.assertEqual(sort_numbers([3, 1, 5]))
        assert [ 'one', 'three', 'five'] == numbers

if __name__ == '__main__':
    unittest.main()
```