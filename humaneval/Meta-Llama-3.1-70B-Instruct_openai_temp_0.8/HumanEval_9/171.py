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

    max_so_far = numbers[0]
    rolling_max_list = [max_so_far]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)

    return rolling_max_list


# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element at index `i` is the maximum value from the original list up to index `i`. It uses a simple iterative approach to achieve this.

Here's a step-by-step explanation of how the script works:

1.  Check if the input list is empty. If it is, return an empty list.
2.  Initialize `max_so_far` with the first element of the input list and `rolling_max_list` with a list containing `max_so_far`.
3.  Iterate through the input list starting from the second element (index 1).
4.  For each element, check if it's greater than `max_so_far`. If it is, update `max_so_far` with the current element.
5.  Append the current `max_so_far` to `rolling_max_list`.
6.  After iterating through the entire list, return `rolling_max_list`.