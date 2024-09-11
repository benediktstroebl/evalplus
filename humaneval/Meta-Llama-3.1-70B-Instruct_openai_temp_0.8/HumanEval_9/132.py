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

    rolling_max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_max_values.append(current_max)

    return rolling_max_values


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the list of rolling maximum values with the first number in the input list and the current maximum value to the first number. Then it iterates over the rest of the input list, updating the current maximum value and the list of rolling maximum values whenever it encounters a number greater than the current maximum. Finally, it returns the list of rolling maximum values.