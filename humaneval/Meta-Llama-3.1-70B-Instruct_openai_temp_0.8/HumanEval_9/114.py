```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers where each element is the maximum of all elements up to that point in the input list.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_maxes = [max_so_far]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_maxes.append(max_so_far)

    return rolling_maxes


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we initialize `max_so_far` with the first element of the input list and append it to `rolling_maxes`. Then we iterate over the rest of the list. If we encounter a number greater than `max_so_far`, we update `max_so_far`. We append `max_so_far` to `rolling_maxes` at each step, resulting in the list of rolling maximums.