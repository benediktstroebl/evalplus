```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)  # [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([1, 2, 3, 4, 5])  # [5, 4, 3, 3, 2, 1]
    >>> rolling_max([5, 6, 7, 8, 9])  # [9, 8, 7, 6, 5]
    >>> 
    """
    return [i for i, n in enumerate(numbers) if n > numbers[i]]
```