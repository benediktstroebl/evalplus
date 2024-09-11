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

    max_elements = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_elements.append(current_max)

    return max_elements

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, the `rolling_max` function iterates through the input list, keeping track of the maximum element encountered so far. The maximum element at each position is appended to the `max_elements` list, which is returned at the end.

This solution has a time complexity of O(n), where n is the length of the input list, since it only requires a single pass through the list. The space complexity is also O(n), as the output list can be at most the same length as the input list.