```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.

    : Returns a : List[int], int] -> List[int]
    :param numbers: list of integers
    :param delimeter: integer
    :return: list of integers
    """
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]
``` 
This code provides a self-contained function that solves the problem of inserting a number delimiter between every two consecutive elements in the input list.