```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in the given list.
    Args: numbers (List[int]): List of integers
    Returns: List[int]: List of rolling maximum elements
    """
    # Convert List[int] to tuple to get wheel index
    numbers = tuple(sorted(numbers))
    return [x for x in numbers if x == numbers[-1]]
```