```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return a list of rolling maximum elements found in a given sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers.append(numbers[-1]) 
    rolling_maxes = [max(numbers[-i:+1] for i in range(len(numbers)-1))]
    return rolling_maxes
```