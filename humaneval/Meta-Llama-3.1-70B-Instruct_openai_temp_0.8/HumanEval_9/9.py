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
    """
    if not numbers:
        return []

    rolling_max_values = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_values.append(max_so_far)

    return rolling_max_values

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function initializes the `rolling_max_values` list with the first element of the input list and then iterates over the rest of the list, updating the `max_so_far` variable whenever a larger number is encountered. The `max_so_far` value is appended to the `rolling_max_values` list at each step. Finally, the function returns the `rolling_max_values` list.

The script includes a docstring that describes the function's behavior and provides an example usage of the function.