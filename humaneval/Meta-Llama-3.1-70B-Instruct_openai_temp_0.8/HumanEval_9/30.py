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
    
    # Initialize an empty list to store the rolling maximum elements
    rolling_maximums = []
    
    # Initialize the maximum element seen so far to negative infinity
    max_so_far = float('-inf')
    
    # Iterate over the input list of numbers
    for num in numbers:
        # Update the maximum element seen so far if the current number is greater
        max_so_far = max(max_so_far, num)
        
        # Append the maximum element seen so far to the list of rolling maximums
        rolling_maximums.append(max_so_far)
    
    # Return the list of rolling maximum elements
    return rolling_maximums

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list, updating the maximum element seen so far and appending it to the list of rolling maximums at each step. The script includes a docstring that describes the function's behavior, and an example usage is provided to demonstrate how to use the function.