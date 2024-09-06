```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list.

    : return theing list of numbers with the specified delimiter between every two consecutive elements.
    >>> delimiter = 4
   
    numbers = [1, 2, 3]
    return [1, 4, 2, 4, 3]
    >>> numbers = [1, 2, 3]
    return [1, 2, 4, 5, 6]
    >>> numbers = [1, 2, 3, 4, 5, 6]
    return [1, 2, Delimiter, 4, 5, 6]
    >>> numbers = [1, 2, 3, 4, 5, 6]
    numbers = [x + i for i, x in enumerate(numbers)]
    return [1, 2, 3, 4, 5, 6] + [4] * 2
    ```