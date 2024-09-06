```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    >>> intersperse([5, 5, 6], 'abc')
    ['abc', 5, 6]
    """
    result = [x, delimeter, x + delimeter] + numbers
    return result
```