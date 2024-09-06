```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('zero nine eight seven six three')
    'zero nine eight seven three'
    >>> sort_numbers('five six three two one')
    'two one three five six'
    >>> sort_numbers('two three four')
    Traceback (most recent call last):
    TypeError: 'str' object does not support item assignment
    """
    numbers = numbers.split()
    required for theuz list to be split.
    numbers = [list(numbers)
    numbers.sort()
    required to be sorted.
# Convert list back string
    numbers = ' '.join(numbers)
    return numbers
```