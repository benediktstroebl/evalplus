```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum element found until given moment
        in the sequence.
    """
    if not numbers:
        return []

    rolling_maxims = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_maxims.append(current_max)

    return rolling_maxims


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found until each moment in the sequence. The function iterates over the input list, keeping track of the current maximum element found so far. If a new maximum element is found, it updates the current maximum and appends it to the result list. Finally, the function returns the list of rolling maximum elements.

The script includes example usage of the `rolling_max` function with the input list `[1, 2, 3, 2, 3, 4, 2]`, which produces the expected output `[1, 2, 3, 3, 3, 4, 4]`.