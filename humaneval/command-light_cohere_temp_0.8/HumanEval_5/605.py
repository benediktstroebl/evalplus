```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list numbers.
    >>> list = [1, 2, 3, 4, 5]
    >>> intersperse(list, 2)
    [1, 2, 2, 3, 4, 5]
    >>> intersperse([1, 2, 3], 1)
    Traceback (most recent call last):
    ...
    ValueError: argument 1 must be a positive integer or None, not '1'
    """
    if not_positive(delimiter):
        raise ValueError("delimiter must be a positive integer or None")
        
    return [num + delimiter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)] + [delimiter] * [len(numbers)]

def not_positive(x: int) -> bool:
    return x > 0
```