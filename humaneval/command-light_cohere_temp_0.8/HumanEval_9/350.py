```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([4, 4, 5])
    [5]
    """
    return [max(numbers[i:], numbers[i+1:]) for i in range(len(numbers)-1)]
```