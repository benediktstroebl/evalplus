```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.

    Parameters:
        numbers (List[int]): list of numbers to be intersppered
        delimiter (int): Insert the number 'delimiter' between every two consecutive elements.

    Returns: a list of numbers with the delimiter inserted.
    >>> intersperse([1, 2, 3], 2)
    [1, 2, 2, 3]
    ```