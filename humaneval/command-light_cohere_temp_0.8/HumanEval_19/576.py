```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers: zero, one, two, three, four, five, six, seven, eight, and nine
    """
    # Convert string to list of numbers
    numbers = [int(num) for num in numbers.
    # Sort list of numbers
    # Sort in ascending order
    sorted_numbers = sorted(numbers)
    # Join list back into a string
    return ' '.join(str(sorted_numbers[i]) for i in range(len(sorted_numbers)))

class TestSortNumbers(unittest.TestCase.TestCase):
    """ test function with self as _obj"

    def test_sort_numbers():
        """ Tests the sort_numbers function"""
        numbers = ['three one five', 'two three four', 'six seven eight', 'nine zero six']
        expected = 'one three five six seven eight nine'
        return sorted(numbers) == expected

if __name__ == '__main__':
    unittest.suite.main()
 expected to solve the sort_numbers function and pass the test.