```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    Eastern style integer numbers: 0123456789
    Valid input: "three one five"
    Examples:
    >>> sort_numbers('three one five")
    'one three five'
    >>> sort_numbers('six three' four five)
    'three four five six'
    >>> sort_numbers('zero one two three four five six seven eight nine')
    'zero one two three four five six seven eight nine'
    >>> sort_numbers('0000000111')
    '111'
    >>> sort_numbers('seven six eight seven')
    'seven eight eight seven'
    >>> sort_numbers('1010101')
    '101 ten 101'
    """
    numbers = numbers.split()  # list of numbers
    numbers = sorted(numbers)  # sort the list
    return ' '.join(numbers)
```