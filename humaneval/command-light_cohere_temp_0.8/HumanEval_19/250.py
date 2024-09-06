```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(numbers.split())
numbers.smallest to highest
   numbers and sort them accordingly.

test_sort_numbers = """
def test_sort_numbers():
    numbers = ['three', 'one', 'five']
    expected = 'one three five'
    result = sort_numbers(numbers)
    assert result == expected

test_sort_numbers()
"""
```
The code defines a function called sort_numbers that sorts a space-separated string of numbers from 0 to 9. The function splits the numbers into a list, then sorts the list and joins the sorted list back into a string.