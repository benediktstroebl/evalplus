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
    # Initialize an empty list to store the rolling maximums
    max_until_now = []
    
    # Initialize the current maximum to negative infinity
    current_max = float('-inf')
    
    # Iterate over each number in the input list
    for num in numbers:
        # Update the current maximum if the current number is greater
        current_max = max(current_max, num)
        
        # Append the current maximum to the list
        max_until_now.append(current_max)
    
    # Return the list of rolling maximums
    return max_until_now

# Example usage
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iterative approach to keep track of the maximum element seen so far and appends it to the result list at each step. The function includes a docstring that provides a description of the function, its arguments, and its return value, as well as an example usage.