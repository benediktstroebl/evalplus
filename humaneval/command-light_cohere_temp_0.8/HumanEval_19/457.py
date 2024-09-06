```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
   ally sorted(nums).
    """

    def test_sort_numbers() -> None:
        """Tests will pass if the output of sort_numbers is correctly sorted"""
        numbers = 'three one five'
        expected = 'one three five'
        actual = sort_numbers(numbers)
        unittest.assert.asserttestarraymodule assert expected actual == expected,

if __name__ == '__main__':
    unittest.main()
```