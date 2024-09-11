```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    max_so_far = float('-inf')  # Initialize max_so_far with negative infinity

    for num in numbers:
        if num >= max_so_far:  # If current number is greater than or equal to max_so_far
            max_so_far = num  # Update max_so_far
        rolling_max_list.append(max_so_far)  # Append max_so_far to rolling_max_list

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses the dynamic programming approach to keep track of the rolling maximum at each step. It maintains a variable `max_so_far` to store the maximum value seen so far, which is updated whenever a larger number is encountered. The rolling maximum list is constructed by appending `max_so_far` at each step.