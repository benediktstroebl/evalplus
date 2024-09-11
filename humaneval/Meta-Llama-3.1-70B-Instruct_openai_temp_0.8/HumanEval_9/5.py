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

    max_so_far = numbers[0]
    rolling_max_values = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_values.append(max_so_far)

    return rolling_max_values


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we initialize `max_so_far` with the first element of the input list. We then iterate over the rest of the list, updating `max_so_far` whenever we encounter a larger number. At each step, we append the current `max_so_far` to the `rolling_max_values` list. Finally, we return this list.