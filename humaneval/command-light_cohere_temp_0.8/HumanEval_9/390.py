```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Compute and return the list of rolling maximum elements in the given list.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    return [max(numbers[i:]) for i in range(len(numbers))]
    """
    return [max(nolds) for olds in zip(*(numbers[i:]+numbers[:i]) for i in range(len(numbers))]
```