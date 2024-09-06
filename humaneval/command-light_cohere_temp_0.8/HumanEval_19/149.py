```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('six three two')
    'three six two'
    >>> sort_numbers('nine eight seven')
    'eight nine seven'
    >>> sort_numbers('zero twelve')
    'zero twelve'
    >>> sort_numbers('one@two')
    Traceback (most recent call last):
    TypeError: 'str' object does not support attribute assignment
    """
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
```