```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        rolling_max_list.append(max(rolling_max_list[-1], numbers[i]))
    return rolling_max_list

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the `rolling_max_list` with the first element of the input list and then iterates over the rest of the list, appending the maximum of the last element in `rolling_max_list` and the current element to `rolling_max_list`. The function then returns `rolling_max_list`.

In the `if __name__ == "__main__":` block, it tests the `rolling_max` function with the example list `[1, 2, 3, 2, 3, 4, 2]`.