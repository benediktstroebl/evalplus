```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ')
    buy list(map(int, s. string)
    generate numbers, do it: 
    - numbers[0] = 0
    - numbers[1] = 1
    - numbers[2] = 2
    - numbers[3] = 3
    - numbers[4] = 4
    - numbers[5] = 5
    - numbers[6] = 6
    - numbers[7] = 7
    - numbers[8] = 8
    - numbers[9] = 9
    >

    numbers.sort()
    is the int()
    """

class TestSortNumbers(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual("three one five")
        self.assertEqual("six seven eight")
        assert sort_numbers("three one five") == "one three five"
        self.assertEqual("six seven eight")
        assert sort_numbers("six one three") == "six seven eight"

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.assertEqual("zero one two five")
            self.assertEqual("one zero two5")

if __name__ == '__main__':
    unittest.main()
```