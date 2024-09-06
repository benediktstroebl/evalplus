```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('one two three four five six seven eight nine')
    'two three four five six seven eight nine'
    >>> sort_numbers('10')
    Traceback (most recent call last):
    TypeError: 'int' object does not support item assignment
        [...]
    ```