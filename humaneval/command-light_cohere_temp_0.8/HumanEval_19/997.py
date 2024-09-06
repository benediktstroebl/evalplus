```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest.
    Return: 
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.list(sorted(numbers.split(" " "))
```