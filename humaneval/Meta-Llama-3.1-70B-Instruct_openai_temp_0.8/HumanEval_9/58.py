```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_values.append(current_max)

    return max_values

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the rolling maximum values. It initializes the `max_values` list with the first number in the input list and keeps track of the current maximum value. Then, it iterates over the rest of the input list, updating the current maximum value whenever it encounters a larger number. Finally, it appends the current maximum value to the `max_values` list. The function returns the `max_values` list.

The script also includes an example usage of the `rolling_max` function, demonstrating its behavior with the input list `[1, 2, 3, 2, 3, 4, 2]`.