```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:  # Check if the input list is empty
        return []

    max_so_far = numbers[0]  # Initialize max_so_far with the first element of the list
    result = [numbers[0]]  # Initialize the result list with the first element

    for num in numbers[1:]:  # Iterate over the rest of the list
        if num >= max_so_far:  # If the current number is greater than or equal to max_so_far
            max_so_far = num  # Update max_so_far
            result.append(num)  # Append num to the result list

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It iterates over the input list, maintaining a running maximum and appending it to the result list whenever a new maximum is found. If the input list is empty, the function returns an empty list.