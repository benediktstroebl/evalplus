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
    max_until_now = float('-inf')
    result = []

    for number in numbers:
        if number >= max_until_now:
            max_until_now = number
        result.append(max_until_now)

    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that calculates the rolling maximum of a given list of integers. It initializes a variable `max_until_now` to negative infinity to ensure that the first number in the list will be greater than it. Then it iterates over the list, updating `max_until_now` whenever it encounters a number that is greater than or equal to the current maximum. The rolling maximum at each position is appended to the result list.