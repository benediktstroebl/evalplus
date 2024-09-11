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

    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(max(result[-1], num))

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum of all elements in the original list up to that point. The function uses a list `result` to build the output list, where `result[-1]` refers to the last element in the list. If the current number is greater than the last element in `result`, it is appended to `result`. Otherwise, the last element in `result` is kept as the maximum value. The function handles the case where the input list is empty by returning an empty list.