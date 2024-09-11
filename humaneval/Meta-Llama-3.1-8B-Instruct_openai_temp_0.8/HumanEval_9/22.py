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
    current_max = float('-inf')  # Initialize current_max as negative infinity

    for num in numbers:
        if num >= current_max:
            current_max = num
        result.append(current_max)

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple and efficient approach to solve the problem. It maintains a `current_max` variable to track the maximum number encountered so far. For each number in the input list, it checks if the number is greater than or equal to the current maximum. If it is, the number is updated as the current maximum. Then, the current maximum is appended to the result list. This way, the result list contains the rolling maximum elements for each position in the input list.