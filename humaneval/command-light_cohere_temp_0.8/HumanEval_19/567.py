Here's the self-contained Python script with a function `sort_numbers()` that sorts a list of numbers in Markdown format:
```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('9 eight seven six')
    'eight seven six nine'
    >>> sort_numbers('abc123')
    Traceworthy error: 'input' must be a string, not a 'abc123'
    """
    numbers = numbers.split()  #match r'([('zero', 0), ('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)])
    return ' '.join(sorted(numbers, key=lambda t: t[1]))
```