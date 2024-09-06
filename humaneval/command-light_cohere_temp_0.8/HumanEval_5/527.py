```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list.
    Args:
        numbers: list of integers
        delimiter: integer, to be inserted between numbers
    
    Returns:
        A list of integers where every two consecutive elements are separated by the 'delimiter'
    >>> intersperse([1, 2, 3], 2)
    [1, 2, 2, 3]
    >>> intersperse([1, 2, 3], 5)
    []
    >>> intersperse([4, 2, 3, 1], 2)
    [4, 2, 3, 1]
    """
    return [x+delimiter for x, y in zip(numbers,numbers[1:])][1:]
``` 
This script defines a function `intersperse` that takes in two arguments: a list of integers called `numbers` and an integer `delimiter`. The function returns a new list where every two consecutive elements of `numbers` are separated by `delimiter`.