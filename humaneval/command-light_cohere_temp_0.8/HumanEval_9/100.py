```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Find the maximum element in a list after applying rolling maximum
    for each index in the list.
   
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x if (x == numbers[i]) else max(numbers[i], x) for x, i in zip(numbers, range(len(numbers)))]
```