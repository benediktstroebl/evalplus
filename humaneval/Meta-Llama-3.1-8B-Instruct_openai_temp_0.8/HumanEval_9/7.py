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

    rolling_max_list = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num >= current_max:
            rolling_max_list.append(num)
            current_max = num
        else:
            rolling_max_list.append(current_max)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that calculates the rolling maximum elements from a given list of numbers. The function initializes the `rolling_max_list` with the first element of the input list and then iterates over the rest of the list. If a number is greater than or equal to the current maximum, it updates the `current_max` and appends the number to the `rolling_max_list`. Otherwise, it appends the `current_max` to the `rolling_max_list`. Finally, it returns the `rolling_max_list`. The script includes an example usage of the function with the input `[1, 2, 3, 2, 3, 4, 2]`.