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

    rolling_max_list = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num >= current_max:
            current_max = num
            rolling_max_list.append(num)
        else:
            rolling_max_list.append(current_max)

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function works by iterating over the input list and updating the `current_max` variable whenever a larger number is encountered. The `rolling_max_list` is updated by appending the `current_max` value whenever a new maximum is found. If a number smaller than the `current_max` is encountered, the `current_max` is appended to the `rolling_max_list` to maintain the rolling maximum. The function returns the `rolling_max_list` at the end.