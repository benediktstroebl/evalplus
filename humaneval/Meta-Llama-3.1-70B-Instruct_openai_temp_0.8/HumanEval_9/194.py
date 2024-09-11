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

    max_vals = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_vals.append(current_max)

    return max_vals


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we initialize `max_vals` with the first element of the input list and `current_max` to keep track of the rolling maximum. We then iterate through the rest of the input list. If a number is greater than the current maximum, we update `current_max`. We append `current_max` to `max_vals` at each iteration. The function returns `max_vals`, which contains the rolling maximum elements.