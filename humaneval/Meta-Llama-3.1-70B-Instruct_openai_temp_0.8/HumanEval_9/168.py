```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum element found until given moment in the sequence.
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of integers representing the rolling maximum element found until each moment in the sequence.

Here's a step-by-step explanation of how the function works:

1.  It first checks if the input list is empty. If it is, the function returns an empty list.
2.  It initializes the `rolling_max_list` with the first element of the input list and sets `max_so_far` to the same value.
3.  It then iterates over the rest of the input list. For each element, it checks if the element is greater than `max_so_far`. If it is, it updates `max_so_far` with the new value.
4.  Regardless of whether `max_so_far` was updated, it appends the current `max_so_far` value to `rolling_max_list`.
5.  Finally, it returns `rolling_max_list`, which contains the rolling maximum element found until each moment in the sequence.

The test case at the end of the script demonstrates the function's behavior with the example input `[1, 2, 3, 2, 3, 4, 2]`, which produces the expected output `[1, 2, 3, 3, 3, 4, 4]`.