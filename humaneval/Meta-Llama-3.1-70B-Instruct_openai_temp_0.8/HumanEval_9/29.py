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

    max_so_far = numbers[0]
    rolling_max_list = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_list.append(max_so_far)

    return rolling_max_list

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the `max_so_far` variable with the first element of the input list and the `rolling_max_list` with the same element. Then it iterates over the rest of the input list, updating `max_so_far` whenever it encounters a larger number, and appending the current `max_so_far` to `rolling_max_list`. Finally, it returns `rolling_max_list`.

The script also includes a docstring that explains the purpose of the function, its parameters, and its return value, and provides an example usage of the function.