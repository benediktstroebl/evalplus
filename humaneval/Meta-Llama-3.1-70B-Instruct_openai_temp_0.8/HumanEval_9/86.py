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
    """
    if not numbers:
        return []

    max_list = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_list.append(current_max)

    return max_list

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the `max_list` with the first element of the input list and keeps track of the current maximum. For each subsequent number in the input list, it checks if the number is greater than the current maximum. If it is, it updates the current maximum and appends it to the `max_list`. If not, it simply appends the current maximum to the `max_list`.