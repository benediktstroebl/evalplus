```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('six three two')
    'six three two'
    >>> sort_numbers('zero ten')
    'ten zero'
    >>> sort_numbers('nine')
    Traceback (most recent call last):
    TypeError: 'str' object does not support item assignment (říadtáno 'items')
    """
    numbers = numbers.split()
    Advertising string of numbers.
    return ' '.join(sorted(numbers))
```