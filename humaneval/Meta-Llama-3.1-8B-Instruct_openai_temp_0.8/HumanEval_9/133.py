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
    max_until_now = numbers[0]  # Initialize max_until_now with the first element
    rolling_max_values = [max_until_now]  # Initialize rolling_max_values with max_until_now

    for num in numbers[1:]:  # Start from the second element
        max_until_now = max(max_until_now, num)  # Update max_until_now
        rolling_max_values.append(max_until_now)  # Append max_until_now to rolling_max_values

    return rolling_max_values

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script uses a simple iterative approach to keep track of the maximum element seen so far, and appends this maximum to the result list at each step. The function has a time complexity of O(n), where n is the length of the input list.