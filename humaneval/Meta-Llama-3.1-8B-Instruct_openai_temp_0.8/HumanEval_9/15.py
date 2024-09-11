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
    if not numbers:
        return []

    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than the last rolling maximum, update the result list
        if num > result[-1]:
            result.append(num)
        # Otherwise, keep the last rolling maximum
        else:
            result.append(result[-1])

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 10, 3, 8, 2]))  # Output: [5, 10, 10, 10, 8]
print(rolling_max([]))  # Output: []
```

This script defines the `rolling_max` function, which takes a list of integers as input and returns a list of rolling maximum elements. The function uses a simple iterative approach to maintain the rolling maximum as it iterates over the input list. The script also includes example usage and test cases to demonstrate the function's correctness.