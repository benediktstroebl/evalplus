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
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function initializes `max_so_far` with the first element of the input list and then iterates through the rest of the list, updating `max_so_far` whenever it encounters a larger number. The current `max_so_far` is appended to the `rolling_max_list` at each step. Finally, the function returns the `rolling_max_list`.

The script includes an example usage of the `rolling_max` function with the input list `[1, 2, 3, 2, 3, 4, 2]`, which produces the expected output `[1, 2, 3, 3, 3, 4, 4]`.