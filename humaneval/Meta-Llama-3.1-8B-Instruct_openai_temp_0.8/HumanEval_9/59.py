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
    current_max = float('-inf')  # Initialize current_max to negative infinity

    for num in numbers:
        if num > current_max:
            current_max = num  # Update current_max if a larger number is found
        result.append(current_max)  # Append current_max to the result list

    return result


# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the rolling maximum (i.e., the maximum element up to that point in the original list). The function iterates through the input list, keeping track of the maximum element seen so far and appending it to the result list. The result list contains the rolling maximum elements for each position in the input list.