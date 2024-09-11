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
    rolling_max_list = []
    max_so_far = float('-inf')

    for num in numbers:
        if num >= max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iteration over the input list, updating the `max_so_far` variable whenever it encounters a larger number, and appending the current `max_so_far` to the `rolling_max_list`. The function is then tested with a sample input.