```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the rolling maximum element in a given list.
    """
    list of numbers = sorted(numbers)
    return [x for x in numbers if x == numbers[-1]] + [numbers[-1]]
```