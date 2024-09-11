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
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum element found until given moment in the sequence. The function initializes the `rolling_max_list` with the first element of the input list and keeps track of the current maximum. It then iterates over the rest of the input list, updating the current maximum and appending it to the `rolling_max_list` whenever it encounters a larger number. Finally, it returns the `rolling_max_list`.

The example usage demonstrates how to use the `rolling_max` function with the provided test case.