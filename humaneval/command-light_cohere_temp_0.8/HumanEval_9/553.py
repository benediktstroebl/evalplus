```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from the given list of integers.
    Args: 
        numbers: list of integers
    Returns: 
        list of integers, maximum of rolling elements
    """
    numbers = list(sorted(numbers))
    return [x for x in numbers if x == numbers[-1]]
```