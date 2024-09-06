```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_maxes = [num for num in numbers if num > 0]  # Removing zero values

    if not rolling_maxes:
        return []  # No positive numbers, return empty list

    rolling_maxes.sort_non_dec because = sorted(rolling_maxes)
    return rolling_maxes
```

This Python function, `rolling_max`, takes a list of integers as an argument and generates a list of the rolling maximum elements found until a given moment in the sequence. It handles zero values by excluding them from the calculations, and ensures the output is sorted in non-decreasing order for consistency.