```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest.
    Return the string with numbers separated by spaces.
    """
example
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.split(' ', ')


numbers_list = ['three', 'one', 'five']
print(sort_numbers(' '.join(numbers_list)))
print(sort_numbers('six seven eight nine'))
```