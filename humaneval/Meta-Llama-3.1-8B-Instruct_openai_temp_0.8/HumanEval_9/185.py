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

    max_so_far = numbers[0]
    result = [numbers[0]]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that calculates the rolling maximum of a given list of integers. It initializes the `max_so_far` variable with the first element of the list and the `result` list with the same element. Then, it iterates over the rest of the list, updating `max_so_far` if a larger number is encountered and appending `max_so_far` to the `result` list. Finally, it returns the `result` list. The script also includes a test case to demonstrate the function's usage.