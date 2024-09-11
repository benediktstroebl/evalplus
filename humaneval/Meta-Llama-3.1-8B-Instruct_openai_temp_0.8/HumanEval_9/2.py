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
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we initialize an empty list `rolling_max_list` to store the rolling maximum elements and a variable `max_so_far` to keep track of the maximum element seen so far. We iterate over each number in the input list, updating `max_so_far` if we find a larger number, and appending the current `max_so_far` to the `rolling_max_list`. Finally, we return the `rolling_max_list`.