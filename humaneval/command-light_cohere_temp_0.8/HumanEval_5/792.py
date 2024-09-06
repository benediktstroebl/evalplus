```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Parameters: numbers (List[int]): The list of integers to be intersphered.
    delimeter: int, The delimiter to be inserted.
    Returns: list<of numbers with the delimiter inserted.
    """
example:
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_list = [num for num in numbers if not next(numbers, delimeter)] + [delimiter] + [num for num in numbers if next(numbers, delimeter)]
    return new_list
```