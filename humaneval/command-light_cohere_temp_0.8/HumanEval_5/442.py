```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Numbers are separated by the minimum of 'delimiter' and 2
    >>> intersperse([1, 2, 3], 2)
    [1, 2, 2, 3]
    >>> intersperse([1, 2, 3], 0)
    [1, 3, 2]
    >>> intersperse([1, 2, 3], infinity)
    [1, 2, 3]
    """
    return [i for i in numbers if i >= delimiter or i + delimiter >= numbers[0]]
```