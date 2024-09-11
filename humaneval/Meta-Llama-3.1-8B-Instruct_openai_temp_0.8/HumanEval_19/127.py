```python
from typing import List, Dict
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): Input string of numbers.

    Returns:
        str: Sorted string of numbers.
    """
    # Define a dictionary to map string numbers to their integer values
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

import unittest

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('nine eight seven'),'seven eight nine')
        self.assertEqual(sort_numbers('four five six'), 'four five six')

if __name__ == '__main__':
    unittest.main()
```

In this script, the `sort_numbers` function takes a string of space-delimited numbers as input and returns the string with numbers sorted from smallest to largest. The function uses a dictionary `num_map` to map string numbers to their integer values, and the `sorted` function with a custom sorting key to sort the list of numbers. The sorted list is then joined back into a string and returned.

The script also includes a unit test case using the `unittest` module to test the `sort_numbers` function with different inputs.