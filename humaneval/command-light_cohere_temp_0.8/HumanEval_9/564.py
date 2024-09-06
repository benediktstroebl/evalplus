```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> numbers[0] = 10
    >>> rolling_max(numbers)
    [10, 3, 3, 3, 4, 4]
    >>> list(numbers)
    [1, 2, 3, 10, 4]
    """
    numbers = List(numbers)
    n = len(numbers)
    return [n + i for i, x in enumerate(numbers) if x > numbers[(i + 1) % n]]
```