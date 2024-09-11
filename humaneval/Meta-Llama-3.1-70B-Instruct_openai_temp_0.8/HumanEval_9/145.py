```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum element found until given moment in the sequence.
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_max_values = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_values.append(max_so_far)

    return rolling_max_values


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Expected output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum element found until given moment in the sequence. It initializes `max_so_far` with the first element of the list and `rolling_max_values` with `max_so_far`. Then, it iterates over the rest of the list, updating `max_so_far` and appending it to `rolling_max_values` whenever it encounters a larger number. Finally, it returns `rolling_max_values`.