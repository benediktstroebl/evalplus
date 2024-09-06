```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of integers representing the rolling maximum elements in the given list.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4]
    """
    return [x for x, i in zip(numbers, numbers) for i in range(len(numbers)) if numbers[i] > x]
```