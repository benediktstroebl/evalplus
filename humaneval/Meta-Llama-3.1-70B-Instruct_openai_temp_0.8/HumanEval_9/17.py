```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    max_element = numbers[0]

    for num in numbers[1:]:
        if num > max_element:
            max_element = num
        rolling_max_list.append(max_element)

    return rolling_max_list

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the `rolling_max_list` with the first element of the input list and sets the `max_element` to the first element. Then, it iterates over the rest of the input list, updating the `max_element` whenever it encounters a larger number and appending the current `max_element` to the `rolling_max_list`. Finally, it returns the `rolling_max_list`.

The script also includes an example usage of the `rolling_max` function with the input `[1, 2, 3, 2, 3, 4, 2]` and prints the output.