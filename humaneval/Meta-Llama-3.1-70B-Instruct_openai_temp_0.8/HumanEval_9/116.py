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

    rolling_maximums = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_maximums.append(current_max)

    return rolling_maximums


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the list of rolling maximums with the first number in the input list and keeps track of the current maximum. It then iterates over the rest of the input list, updating the current maximum and appending it to the list of rolling maximums whenever it encounters a larger number. The function returns the list of rolling maximums.

The script also includes an example usage of the `rolling_max` function with the input list `[1, 2, 3, 2, 3, 4, 2]`, which produces the expected output `[1, 2, 3, 3, 3, 4, 4]`.