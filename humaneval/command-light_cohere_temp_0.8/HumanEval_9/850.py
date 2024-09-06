```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from the given list of integers.
    Returns the maximum element in the sequence of elements after applying rolling maximum.
    """
    maximum element at a given moment in the sequence.
    """
    list of rolling maximum elements: [3, 3, 3, 4, 4]
    """
    numbers = [3, 3, 3, 4, 4, 2, 1, 3]
    return [max(numbers[i:]) for i in range(len(numbers))]
```