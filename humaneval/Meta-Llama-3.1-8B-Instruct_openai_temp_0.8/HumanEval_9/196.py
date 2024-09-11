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
    max_so_far = float('-inf')  # Initialize max_so_far to negative infinity

    for num in numbers:
        if num >= max_so_far:
            max_so_far = num  # Update max_so_far if current number is greater
        result.append(max_so_far)  # Append the current max_so_far to the result

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a variable `max_so_far` to keep track of the maximum element seen so far, and appends this value to the result list for each number in the input list. The result is a list where each element is the maximum of all elements up to that point in the original list.