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
    current_max = float('-inf')  # Initialize current max as negative infinity

    for num in numbers:
        if num > current_max:
            current_max = num  # Update current max if new number is greater
        rolling_max_list.append(current_max)  # Append current max to result list

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which iterates over the input list and keeps track of the maximum number encountered so far. It uses a list `rolling_max_list` to store the rolling maximum elements and returns this list at the end. The function is then tested with a sample list of numbers.