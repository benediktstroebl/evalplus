```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum element found until given moment in the sequence.
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum value encountered so far in the original list. The function uses a simple iterative approach to achieve this. It initializes the `rolling_max_list` with the first element of the input list and keeps track of the maximum value encountered so far in the `max_so_far` variable. Then, it iterates over the rest of the input list, updating `max_so_far` whenever it encounters a larger value and appending the current `max_so_far` to `rolling_max_list`. Finally, it returns `rolling_max_list`.