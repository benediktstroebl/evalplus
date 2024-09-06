```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    >>> intersperse([1,2,3],4)
    [1, 4, 2, 4, 3]
    >>> intersperse([5,2,9,1],4)
    [5, 9, 4, 2, 4, 1]
    """
    new_list = [num + delimeter if num != delimeter else num for num in numbers]
    return new_list
```