```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Numbers are separated by at least index.
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    >>> intersperse([1, 2, 3], 100)
    []
    >>> intersperse([10, 20, 30], 10)
    [10, 20, 30]
    """
    new_list = [num for num in numbers if num != delimeter]
    new_list.append(delimiter)
    new_list.append(num)
    new_list.append(delimiter)
    return new_list
```