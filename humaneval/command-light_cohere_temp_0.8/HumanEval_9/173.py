```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until a given moment
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> numbers = [10, 20, 30, 10, 40, 30, 20, 10]
    >>> rolling_max(numbers)
    [10, 20, 30, 30, 40, 20, 10]
    """
    l = []
    while numbers:
        if numbers[0] > l[-1]:
            l.append(numbers[0])
        numbers = numbers[1:]
    return l
```