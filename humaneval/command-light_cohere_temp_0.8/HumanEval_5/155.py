```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Args: numbers (List[int]): A list of integers.
    Returns: a list of integers with a delimiter inserted between every two consecutive elements.
    """
    """
    test cases:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    >>> intersperse([1, 9, 4, 8, 7], 3)
    [1, 3, 7, 9, 4]
    """
    return [i + delimeter for i,j in zip(numbers,numbers[1:]+[delimeter]) for j in numbers]
```