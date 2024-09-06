```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list. """
    return theall numbers with a specified delimiter.
    >>> intersperse([1, 2, 3], ' ')
    ['1', '2', '3']
    >>> intersperse([1, 2, 3], 'x')
    Traceback (most recent call last):
    TypeError: 'str' object does not support attribute 'append'
    """
    return [x + delimeter if i < len(numbers) - 1 else x for i, x in enumerate(numbers)]
```