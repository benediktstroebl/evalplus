```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximum at each index.

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    # Initialize the result list with the first element
    result = [numbers[0]]

    # Iterate through the list starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than the last element in the result list,
        # update the result list with the current number
        if num > result[-1]:
            result.append(num)
        # Otherwise, keep the last element in the result list
        else:
            result.append(result[-1])

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function initializes the result list with the first element of the input list and then iterates through the rest of the list. If the current number is greater than the last element in the result list, it updates the result list with the current number. Otherwise, it keeps the last element in the result list. The function finally returns the result list. The script includes a test case to demonstrate the function's usage.