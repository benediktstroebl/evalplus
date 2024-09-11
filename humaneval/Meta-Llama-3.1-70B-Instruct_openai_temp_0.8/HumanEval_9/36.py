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

    max_elements = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_elements.append(current_max)

    return max_elements


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the rolling maximum elements. The function iterates through the input list, keeping track of the current maximum element. If a new maximum element is found, it updates the `current_max` variable. The function appends the `current_max` value to the `max_elements` list at each step. The function returns the `max_elements` list.

The script also includes an example usage of the `rolling_max` function with the provided test case.