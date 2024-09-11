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
    max_so_far = float('-inf')  # Initialize max_so_far as negative infinity
    result = []  # Initialize an empty list to store the result

    for num in numbers:
        # For each number in the list, update max_so_far if the current number is greater
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)  # Append the updated max_so_far to the result list

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that calculates the rolling maximum for a given list of numbers. It initializes `max_so_far` as negative infinity and iterates over each number in the list, updating `max_so_far` if the current number is greater. The updated `max_so_far` is then appended to the result list. Finally, the script tests the function with the provided example.