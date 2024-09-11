```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Example use case:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum value encountered up to that point in the input list. It uses a simple iterative approach to keep track of the current maximum value and appends it to the result list at each step.

The time complexity of this function is O(n), where n is the length of the input list, because it makes a single pass through the input list. The space complexity is also O(n), because it creates a new list of the same length as the input list.