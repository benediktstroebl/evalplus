```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers as input and returns a list of the rolling max elements found in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x, n in zip(numbers, numbers[1:]) if n > x]
```