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
        if num >= current_max:  # If current number is greater than or equal to current max
            current_max = num  # Update current max
        rolling_max_list.append(current_max)  # Append current max to the list

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list and updates the current maximum value whenever a larger number is encountered. The current maximum value is then appended to the output list.