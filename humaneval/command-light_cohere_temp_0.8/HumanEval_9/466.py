```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers=[1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)  [1, 2, 3, 3, 3, 4, 4]
    """
    max_roll = numbers[0]
    start = 0
    current = numbers[0]

    for num in numbers[1:]:
        current = max(current, num)
        start = (start + 1) % len(numbers)
        max_roll = max(max_roll, current)

    return [start, max_roll]
```