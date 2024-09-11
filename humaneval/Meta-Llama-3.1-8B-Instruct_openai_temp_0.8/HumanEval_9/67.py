```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_so_far = float('-inf')  # Initialize max_so_far as negative infinity

    for num in numbers:
        if num >= max_so_far:
            max_so_far = num  # Update max_so_far if current number is greater
        result.append(max_so_far)  # Append max_so_far to the result list

    return result
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes `max_so_far` as negative infinity and iterates over the input list. For each number, if it's greater than or equal to `max_so_far`, it updates `max_so_far`. Finally, it appends `max_so_far` to the result list and returns the result list.