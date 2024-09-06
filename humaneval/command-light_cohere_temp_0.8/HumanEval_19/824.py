```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('six three eight')
    'three six eight'
    >>> sort_numbers('nine eight seven')
    'eight nine seven'
    >>> sort_numbers('ten nine eight six')
    'nine ten eight six'
    >>> sort_numbers('zero three two')
    'zero three two'
    """
    numbers = [int(num) for num in numbers. numbers.sort()
   ized_numbers.title()
   es 'one two' three', 'four', 'five', 'six', 'seven', 'eight', 'nine'.

def test_sort_numbers() -> None:
    numbers = ['three', 'one', 'five', 'six', 'two', 'seven', 'eight', 'four', 'nine']
    expected = ['one', 'three', 'five', 'six', 'seven', 'eight', 'four', 'nine']
    got = sort_numbers(numbers)
    assert expected == got
```