```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine. Valid choices are names are list of numbers.
    Return numbers sorted from smallest to largest.
    e.g. sort string 	 a-- works on strings with numbers from zero to nine, and the numbers are case insensitive.
    >>> test_sort_numbers('three one five')
    'one three five'
    """
    return numbers.split(' ')'.sort_keys(numbers.split(' ' '))[::-1]

# add unit tests using pytest

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
```