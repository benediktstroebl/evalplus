```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    >>> numbers = [1, 2, 3, 4]
    >>> delimiter = 2
    >>> result = intersperse(numbers, delimiter)
    [1, 2, 2, 3, 4]
    >>> result == [1, 2, 2, 3, 4]
    True
    >>> numbers = [1, 2, 3, 4, 5]
    >>> delimiter = 3
    >>> result = intersperse(numbers, delimiter)
    [1, 4, 7, 10, 12]
    >>> result == [1, 4, 7, 10, 12]
    True
    """
    return [x + i for i, x in enumerate(numbers, delimeter)]

# Test
numbers = [1, 2, 3, 4]
delimiter = 2
result = intersperse(numbers, delimiter)
print(result == [1, 2, 2, 3, 4])
```