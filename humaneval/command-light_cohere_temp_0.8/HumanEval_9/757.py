```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Returns the list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)  # [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([4, 4, 5]) # [5, 5, 5]
    >>> rolling_max([1, 2, 3, 2, 3, 4, 3, 2, 1]) # [2, 3, 3, 3, 2, 1, 2]
    >>> rolling_max([5, 1, 2, 3, 4, 3, 2]) 
    [5, 5, 5]
    """
    l = [x for x in numbers]
    # build the rolling window
    for i in range(1, len(l)):
        l[i] = max(l[i-1], l[i])
    return l
```