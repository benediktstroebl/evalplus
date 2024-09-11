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
        if num >= max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 3, 1, 4, 2]))  # [5, 5, 5, 5, 4]
print(rolling_max([]))  # []
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It first checks if the input list is empty, in which case it returns an empty list. Otherwise, it initializes the maximum element `max_so_far` to the first element of the list and adds it to the result list. Then it iterates over the rest of the list, updating `max_so_far` whenever it encounters a larger element and appending the current `max_so_far` to the result list. Finally, it returns the result list. The script also includes some test cases to demonstrate the function's behavior.