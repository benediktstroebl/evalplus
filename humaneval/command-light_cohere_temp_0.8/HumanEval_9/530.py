```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    rolling_max([1, 2, 3, 3, 3, 4, 4])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = List(numbers)
    return [x for x in numbers if x > numbers[-1]]
```