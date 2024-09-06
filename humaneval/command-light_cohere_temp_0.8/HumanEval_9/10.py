```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of integers representing the rolling maximum element(s) found until a given moment in the sequence.
    Args: 
        - numbers: a list of integers, 
            e.
        Returns: list of integers, where the maximum element from each window is returned.
    """
    return numbers[:-1] + [max(numbers[i:]) for i in range(len(numbers))]]
```