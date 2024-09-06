```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    This function generates a list of rolling maximum elements in the given list.
    Each element in the list is first compared with the maximum seen so far, 
    then the maximum is updated with the current element, and the 
    maximum rolling value is returned.
    """
    list of rolling maxes until given list is returned. 
"""
    numbers = [1, 2, 2, 3, 3, 4, 2, 3, 4, 1]
    return [x for x, _ in zip(numbers, numbers[1:])]
```