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

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max()` that takes a list of integers as input and returns a list of rolling maximum elements. The function initializes the maximum so far to the first element of the input list and the result list with the maximum so far. It then iterates over the rest of the input list, updating the maximum so far to be the maximum of the current maximum so far and the current number, and appending the updated maximum so far to the result list. If the input list is empty, the function returns an empty list.