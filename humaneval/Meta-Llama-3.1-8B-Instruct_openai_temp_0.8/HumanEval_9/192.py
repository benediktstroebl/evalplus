### Rolling Maximum List Generator

Here's a Python function that generates a list of rolling maximum elements from a given list of integers.

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

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')  # Initialize maximum value as negative infinity
    max_list = []

    for num in numbers:
        if num >= max_so_far:  # If current number is greater than max_so_far
            max_so_far = num  # Update max_so_far
        max_list.append(max_so_far)  # Append max_so_far to max_list

    return max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This function iterates over each number in the input list, updating `max_so_far` whenever it encounters a larger number. It then appends `max_so_far` to the `max_list`. This process is repeated until all numbers in the list have been processed, resulting in a list of rolling maximum elements.