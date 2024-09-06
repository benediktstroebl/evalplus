```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Find the maximum element in the list after each element is added
    >>> # [1, 2, 3, 2, 3, 4, 2] rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 4, 4]
    """
    return [max(numbers + [0]) for _ in range(len(numbers))]] + [max(numbers)]
```