```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates and returns the rolling maximum element found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers.append(max(numbers[:-1]))
    return numbers
```