### Rolling Maximum Element
#### A Python Script to Calculate Rolling Maximum Elements in a List

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
    if not numbers:
        return []

    rolling_max_list = []
    current_max = float('-inf')

    for num in numbers:
        if num >= current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list, keeping track of the current maximum element found so far. For each element in the list, it checks if the element is greater than or equal to the current maximum. If it is, the element becomes the new current maximum. The function then appends the current maximum to the result list. Finally, the function returns the result list.