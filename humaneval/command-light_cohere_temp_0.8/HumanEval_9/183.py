```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Compute the rolling maximum element in a list of integers.
    Returns a a list of maximum elements, starting from the first element and rolling through the list.
    """
    maximum element in numbers,
    """
    return [num for num, i in zip(numbers, numbers[1:]) if i < len and num > numbers[i]]
```