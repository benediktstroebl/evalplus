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

    rolling_max_values = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_values.append(max_so_far)

    return rolling_max_values

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we initialize the `rolling_max_values` list with the first element of the input list and set `max_so_far` to the first element. Then, we iterate over the rest of the input list. If we encounter a number greater than `max_so_far`, we update `max_so_far`. We append `max_so_far` to `rolling_max_values` at each step, ensuring that we always store the maximum value seen so far in the sequence.