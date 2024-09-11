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

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Check if input list is empty
    if not numbers:
        return []

    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # Update the last element in the result list with the maximum of the current number
        # and the last element in the result list
        result.append(max(num, result[-1]))

    return result


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. It iterates over the input list and updates the last element in the result list with the maximum of the current number and the last element in the result list. The function returns the result list. The script also includes a test case to demonstrate the function's usage.