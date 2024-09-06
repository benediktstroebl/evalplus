```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> numbers = [5, 10, 6, 8, 4, 2]
    >>> rolling_max(numbers, 4)
    [10, 8, 6, 4]
    """
    return [x for x, _ in enumerate(sorted(numbers)) if numbers[x] > numbers[x+1]]
```