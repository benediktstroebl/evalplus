**Rolling Maximum Element**
==========================

The following Python function calculates the rolling maximum element in a given list of integers.

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum element.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        rolling_max_list.append(max(rolling_max_list[i-1], numbers[i]))
    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a dynamic approach, initializing the `rolling_max_list` with the first element of the input list. Then, for each subsequent element, it appends the maximum between the last element in `rolling_max_list` and the current element. The function returns the `rolling_max_list` after processing the entire input list.