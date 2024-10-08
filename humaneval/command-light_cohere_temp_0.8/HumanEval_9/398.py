```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Returns a list of rolling maximum elements in a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [num for num, _ in sorted((num, num + 1), reverse=True)]
```