Here's a self-contained Python function that solves the problem of finding the maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [n for n, i in zip(numbers, numbers[1:])
            for i in range(1, len(numbers) // 2 + 1)]
```
The function takes a list of integers and returns a list of the maximum elements found after applying the rolling effect.