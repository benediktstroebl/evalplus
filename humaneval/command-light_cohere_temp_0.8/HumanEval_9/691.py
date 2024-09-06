```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from a given list of integers.
    Returns the max elements with a rolling effect from the original list.
    """
    maxes = [num for num in numbers for _ in range(len(numbers))] 
    return [maxes[i] for i in range(len(numbers))]
    """
    return [maxes[i] for i, maxes in enumerate(maxes)]
```