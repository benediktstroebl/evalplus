```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers

    Returns:
    List[int]: A list of rolling maximum elements

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]
    
    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # The rolling maximum at each position is the maximum of the current number and the rolling maximum at the previous position
        result.append(max(num, result[-1]))
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses the `max` function to calculate the rolling maximum at each position by comparing the current number with the rolling maximum at the previous position. The script also includes a test case to demonstrate the functionality of the `rolling_max` function.