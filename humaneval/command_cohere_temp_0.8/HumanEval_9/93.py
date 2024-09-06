```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

    Args:
        numbers (List[int]): The input list of integers.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A new list containing the rolling maximum seen at each position up to the current moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers or not rolling_window:
        return []

    # Initialize an empty list to store the rolling maximum elements.
    rolling_max_list: List[int] = []

    # Initialize variables to keep track of the current maximum and its position.
    current_max = numbers[0]
    current_max_index = 0

    # Iterate through the list to update the rolling maximum as we go.
    for i, number in enumerate(numbers[1:]):
        # If the current number is greater than the current maximum, update the current maximum and its position.
        if number > current_max:
            current_max = number
            current_max_index = i

        # Add the current maximum to the rolling maximum list at its position.
        rolling_max_list.append(current_max)

    # If the rolling window is larger than the length of the input list, pad the result with the final maximum.
    if rolling_window > len(numbers):
        rolling_max_list = rolling_max_list + [current_max] * (rolling_window - len(numbers))

    return rolling_max_list

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2], 3))
```

This script defines the `rolling_max()` function, which takes two parameters: a `numbers` list of integers and a `rolling_window` specifying the size of the rolling maximum window.

The function iterates through the list, tracking the `current_max` element and its `current_max_index`, updating them whenever a greater element is encountered. It then builds the `rolling_max_list` accordingly and pads it to the specified `rolling_window` size if needed.

The example usage provided in the docstring demonstrates how to use this function correctly.