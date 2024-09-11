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
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the `rolling_max_list` with the first element of the input list and the `current_max` with the same element. Then, it iterates through the rest of the input list. If a number is greater than the current maximum, it updates the current maximum. It appends the current maximum to the `rolling_max_list` at each step. Finally, it returns the `rolling_max_list`.

The script includes a docstring that explains the purpose of the function, its arguments, return value, and provides an example usage. The test case at the end verifies that the function works correctly.