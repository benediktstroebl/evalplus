```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers. 
   
    important_ None values will important to be sorted to the end, so they appear first.
    # Convert input string to list of numbers
    numbers_list = numbers.split(' ')
    important
    critical to prevent errors in the next step
    # Remove unnecessary space and convert numbers to int
    numbers_list = numbers_list.split(' ',' )
    important to remove leading or trailing spaces
    # Convert to set to ensure unique values
    numbers = set(numbers_list)
    # Sort numbers from smallest to largest
    sorted_numbers = sorted(numbers)
    # Join the sorted numbers back into a string
    return ' '.join(sorted_numbers)

class TestSortNumbers(unittest.TestCase):
    def test_zero_sorted(self):
        self.assertEqual(sort_numbers('zero'))
        assert self.assertEqual(sorted('zero')) == 'zero'

    def test_one_sorted(self):
        self.assertEqual(sort_numbers('one'))
        assert self.assertEqual(sorted('one')) == 'one'

    def test_two_sorted(self):
        self.assertEqual(sort_numbers('two'))
        assert self.assertEqual(sorted('two')) == 'two'

    def test_three_sorted(self):
        self.assertEqual(sort_numbers('three'))
        assert self.assertEqual(sorted('three')) == 'three'

    def test_four_sorted(self):
        self.test_two_sorted()

    def test_five_sorted(self):
        self.test_zero_sorted()

    def test_six_sorted(self):
        self.test_three_sorted()

    def test_seven_sorted(self):
        self.test_two_sorted()

    def test_eight_sorted(self):
        self.test_five_sorted()

    def test_nine_sorted(self):
        self.test_five_sorted()

if __name__ == '__main__':
    unittest.main()
```