```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """
    Returns aIf a list of integers and the delimiter is an integer, it will insert the delimiter as a string.
    >>> type(numbers)  # [int64]
    >>> type(delimiter)  # [int]
    >>> intersperse([1, 2, 3], '!)
    [1!, 2!, 3!
    >>> intersperse([1, 2, 3], '23')
    [1, 23, 2, 23, 3]
    >>> intersperse([1, 9, 5], 'ad')
    ['ad', 1, 'ad', 5]
    >>> intersperse([10, 20, 30], '-')
    [10-, 20-, 30]
    """
    numbers = [x for x in numbers if type(x) == int]
    return [x + delimiter for x, delimiter in zip(numbers, [delimeter] * 2)]
```