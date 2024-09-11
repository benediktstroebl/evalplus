```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum element found until given moment in the sequence.
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

In this script, the `rolling_max` function initializes a list `max_values` with the first element of the input list `numbers`. Then, it iterates through the rest of the list, updating the `current_max` value whenever it encounters a larger number. The `current_max` value is appended to the `max_values` list at each iteration. Finally, the function returns the `max_values` list.