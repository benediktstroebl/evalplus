```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [num for num, i in reversed(zip(numbers, numbers[1:])) if i == 0 or num > numbers[i]]
```
This solution provides a self-contained Python function that uses a list of integers and returns a new list containing the rolling maximum elements found up to a given moment within the sequence.