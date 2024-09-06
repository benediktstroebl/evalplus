```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements.
    >>> numbers = [1, 2, 3, 4, 5]
    >>> rolling_max(numbers)
    [1, 3, 4, 5]
    """
    return [x for x, i in zip(numbers, numbers[1:])][::-1]
```