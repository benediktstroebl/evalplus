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

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input. It initializes the `result` list with the first element of the input list and the `max_so_far` variable with the same value. Then it iterates over the rest of the list. If it encounters a number greater than `max_so_far`, it updates `max_so_far` with this number. In each iteration, it appends `max_so_far` to the `result` list. Finally, it returns the `result` list. The test at the end demonstrates the function's usage and output.