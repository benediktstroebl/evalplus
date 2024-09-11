```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers where each element is the maximum of all elements up to that point in the input list.
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_max_values = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_values.append(max_so_far)

    return rolling_max_values


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum of all elements up to that point in the input list. The function initializes `max_so_far` with the first element of the input list and then iterates over the rest of the list, updating `max_so_far` whenever it encounters a larger number. The current `max_so_far` is appended to the `rolling_max_values` list at each step. Finally, the function returns the `rolling_max_values` list.

The script also includes an example usage of the `rolling_max` function with a sample input list. The output of the script is the expected rolling maximum values for the given input.