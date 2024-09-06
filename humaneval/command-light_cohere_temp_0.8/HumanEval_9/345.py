```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)  # [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([1, 2, 3, 4, 5])  # []
    >>> rolling_max([1, 2, 3, 3, 4, 5])  # [3, 3, 4, 4, 5]
    >>> rolling_max([10, 3, 2, 1])   # [10]
    >>> rolling_max([1, 2, 3, 4, 5, 6])  # [1, 2, 3, 4]
    """
    return [x for x in numbers if x > numbers[-1]]
```