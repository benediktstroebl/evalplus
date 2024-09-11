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
    max_so_far = float('-inf')  # Initialize max_so_far as negative infinity

    for num in numbers:
        max_so_far = max(max_so_far, num)  # Update max_so_far if current num is greater
        rolling_max_list.append(max_so_far)  # Append max_so_far to rolling_max_list

    return rolling_max_list

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print("Rolling max list:", result)
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iterative approach to keep track of the maximum element seen so far. The example usage demonstrates how to call the function with a sample input list and print the resulting rolling max list.