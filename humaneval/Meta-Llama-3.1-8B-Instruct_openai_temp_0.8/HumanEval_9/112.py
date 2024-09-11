### Rolling Maximum Problem Solution
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
    result = [numbers[0]]  # Initialize the result list with the first number
    max_so_far = numbers[0]  # Initialize max_so_far with the first number

    for num in numbers[1:]:  # Iterate over the list starting from the second number
        if num >= max_so_far:  # If current number is greater than max_so_far
            max_so_far = num  # Update max_so_far
        result.append(max_so_far)  # Append max_so_far to the result list

    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple iteration through the list to keep track of the maximum number seen so far. When it encounters a number greater than the current maximum, it updates the maximum and also appends the updated maximum to the result list. This process continues until the entire list has been processed.