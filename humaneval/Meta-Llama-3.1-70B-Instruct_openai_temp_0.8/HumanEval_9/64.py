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

    max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_values.append(current_max)

    return max_values


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 4, 3, 2, 1]))  # [5, 5, 5, 5, 5]
print(rolling_max([1, 1, 1, 1, 1]))  # [1, 1, 1, 1, 1]
print(rolling_max([]))  # []
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of the rolling maximum values. The function iterates over the input list, keeping track of the current maximum value and appending it to the result list at each step. The function also includes a docstring and some example use cases.