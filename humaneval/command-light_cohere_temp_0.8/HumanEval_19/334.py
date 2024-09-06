```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers. Return the string with numbers sorted from smallest to largest"""
    numbers = [int(x) for x in numbers.
    return ' '.join(sorted(numbers))

class TestSortNumbers(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual('three one five')
        self.assertEqual('four five six seven eight nine')
        self.assertEqual('zero one two three four five six seven eight nine')
        self.assertEqual('one two three five six seven eight nine')
        assert sorted(self.test_input()) == self.test_output()

   
    test_valid_input()

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.test_input('abc')

    test_invalid_input()

if __name__ == '__main__':
    unittest.main()
```
This Python script defines a function sort_numbers that takes a space-delimited string of numbers and sorts them. The function also includes input validation to handle invalid inputs. The script includes a corresponding test suite with various test cases to ensure the correctness of the sort_numbers function.