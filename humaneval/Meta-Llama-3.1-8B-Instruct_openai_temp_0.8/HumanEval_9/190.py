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
    if not numbers:
        return []

    max_at_each_point = [numbers[0]]
    for num in numbers[1:]:
        max_at_each_point.append(max(max_at_each_point[-1], num))

    return max_at_each_point

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a list `max_at_each_point` to keep track of the maximum element seen at each point. The function then iterates over the input list, updating `max_at_each_point` at each step. Finally, it returns `max_at_each_point`. The script includes a test case to demonstrate the function's behavior.