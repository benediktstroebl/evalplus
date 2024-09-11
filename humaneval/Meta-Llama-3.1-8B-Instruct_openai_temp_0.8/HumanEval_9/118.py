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

    max_so_far = numbers[0]
    result = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)

    return result
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iterative approach to keep track of the maximum element seen so far and append it to the result list. The function first handles the edge case where the input list is empty, and then initializes `max_so_far` with the first element of the list and adds it to the result list. In the main loop, it updates `max_so_far` with the maximum of the current `max_so_far` and the current number, and appends `max_so_far` to the result list.