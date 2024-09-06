```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list with the rolling maximum element in each moment of a sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = List(numbers) + [float("inf")]
    return [x for x in numbers if x > numbers[-1]]
```