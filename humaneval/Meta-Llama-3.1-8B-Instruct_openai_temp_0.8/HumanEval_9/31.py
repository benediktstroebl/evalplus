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
    current_max = float('-inf')

    for num in numbers:
        # Update the current maximum if the current number is larger
        if num > current_max:
            current_max = num
        # Append the current maximum to the rolling maximum list
        rolling_max_list.append(current_max)

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which takes a list of integers as input and returns a list of rolling maximum elements. The function iterates through the input list, updating the current maximum and appending it to the rolling maximum list at each step. The script includes a test case to demonstrate the function's behavior.