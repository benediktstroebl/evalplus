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
    current_max = float('-inf')  # Initialize with negative infinity

    for num in numbers:
        if num >= current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple iteration over the input list. It maintains a `current_max` variable, which is updated whenever a new maximum value is encountered in the list. The `rolling_max_list` is then populated by appending the current maximum value at each step.