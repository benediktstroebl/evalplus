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

    max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_values.append(current_max)

    return max_values


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we initialize `max_values` with the first element of the input list and set `current_max` to the same value. Then we iterate through the rest of the list. If we find a number that is greater than `current_max`, we update `current_max`. We append `current_max` to `max_values` at each step. The result is a list of rolling maximum elements.