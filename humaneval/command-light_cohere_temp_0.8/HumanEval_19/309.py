```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers: zero one two three four five six seven eight nine
    >>> sorted([0,3,1,5])
    [0,3,1,5]
    >>> sorted([3, 'one',5])
    ['one', 'three', 'five']
    >>> sorted([5, 2, 7, 1])
    [7,5,2]
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('zero eight seven six nine')
    'zero eight seven six nine'
    >>> sort_numbers('four six')
    Traceback (most recent call last):
    TypeError: 'str' object does not support item assignment
    ```