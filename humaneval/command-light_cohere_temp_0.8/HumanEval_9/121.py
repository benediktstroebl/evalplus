```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([5, 15, 8, 12])
    [15, 12, 15]
    """
    return [x for x, i in zip(numbers, numbers[1:]) if i == numbers[0]]
```