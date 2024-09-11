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
    rolling_max_list = []
    max_seen = float('-inf')

    for num in numbers:
        if num >= max_seen:
            max_seen = num
        rolling_max_list.append(max_seen)

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a variable `max_seen` to keep track of the maximum element seen so far, and appends this maximum element to the `rolling_max_list` at each step. If a new maximum element is found, it updates `max_seen` with this new element. The function returns the `rolling_max_list` after processing all numbers in the input list.