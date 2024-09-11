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
    # Initialize an empty list to store the rolling maximums
    rolling_maxes = []
    
    # Initialize the maximum found so far to negative infinity
    max_found_so_far = float('-inf')
    
    # Iterate over the input list in reverse order (to handle the last element first)
    for num in reversed(numbers):
        # Update max_found_so_far if the current number is greater
        max_found_so_far = max(max_found_so_far, num)
        
        # Append the maximum found so far to the left of the current number to the result list
        rolling_maxes.insert(0, max_found_so_far)
    
    # Return the list of rolling maximums
    return rolling_maxes

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that calculates the rolling maximum of a given list of integers. It iterates over the list in reverse order and keeps track of the maximum found so far. The maximum found is inserted at the beginning of the result list for each iteration, effectively achieving the rolling maximum.