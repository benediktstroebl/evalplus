```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    >>> intersperse([1,2,3], 2) 
    [1, 2, 2, 3]
    >>> intersperse([3,2,1],3) 
    [3, 2, 1, 3]
    """ 
    return [i+delimeter if i<len(numbers)-1 else i for i in numbers]
```