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

    rolling_max_list = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function that takes a list of integers as input and returns a list of rolling maximum elements. The function initializes the `rolling_max_list` with the first element of the input list and keeps track of the maximum element encountered so far. It iterates over the rest of the input list, updating the maximum element if a larger number is found and appending the current maximum to the `rolling_max_list`. The function returns the `rolling_max_list`. The example usage demonstrates how to call the function with a sample input list.