```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    numbers.sort()
    neither sorted numbers list, nor str. Convert back list list back into string.
    """ The strings to list
    and convert numbers to int
    list(numbers).numbers.numbers.sort()
    Bah!/
   
filtered list with invalid choices)
    return list(numbers).filter(str.join[9 list is filtered numbers))
test_sort_numbers = unittest.TestCase()()
def verify_numbers(numbers: List[int]) -> None:
    # numbers = 'three one five'
    # verify_numbers([0, 1, 2, 3, 5])
    # test_sort_numbers.verify_numbers([2, 3, 5])
    # verify_numbers([2, 3, 5, 1, 8])

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers_valid(self):
        self.assertEqual(sorted(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))
        self.assertEqual(sorted(['zero', 'two', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))

    def test_sort_numbers_invalid(self):
        self.assertEqual(sorted(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'eight', 'nine']))

if __name__ == "__main__":
    unittest.main()
```