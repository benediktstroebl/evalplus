```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [num for num, idx in zip(numbers, numbers) for idx, n in enumerate(numbers) if n >= numbers[idx] and idx not in numbers[-1:2]]
```