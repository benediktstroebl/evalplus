```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Example lists with consecutive numbers like `[1, 2, 3, 4]`
    >>> intersperse([1, 2, 3, 4], 2)
    [1, 2, 2, 3, 4]
    >>> intersperse([1,2,3,4,5],1)
    Traceback (most recent call last):
    ...
    ValueError: unexpected input type ('int', ...)
    expected 'List[int]'
    """
    result = [i + delimeter for i, j in zip(numbers, numbers[1:])] + [numbers[-1]]
    return result

# Unit tests:
numbers = [1, 2, 3, 4]
delimiters = [2, 2, 2]

expected = [1, 2, 2, 3, 4]
print(f'Expected: {expected})
result = intersperse(numbers, delimiters)
print(f'Result: {result})
```