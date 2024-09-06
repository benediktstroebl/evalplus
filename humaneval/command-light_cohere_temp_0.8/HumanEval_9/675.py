```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until a given moment
    in the sequence (default is 0).
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x,i in zip(numbers, numbers[1:])][::-1][i+1:]
```
This code solves the problem of finding the rolling maximum elements in a list of integers, by using a generator expression.