```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    Args:
        numbers: list of integers
    Returns: list of integers
    """
    numbers = sorted(numbers)
    rolling_max_elements = [x for x in numbers if x == numbers[-1]] + [numbers[-1]]
    return rolling_max_elements
```