```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    Args:
    numbers: A list of integers.
    
    Returns:
    A list of integers representing the rolling maximum elements.
    """
    
    # Initialize an empty list to store the rolling maximum elements
    rolling_max_elements = []
    
    # Initialize the maximum element seen so far to negative infinity
    max_so_far = float('-inf')
    
    # Iterate over the input list of numbers
    for num in numbers:
        # Update the maximum element seen so far if the current number is greater
        max_so_far = max(max_so_far, num)
        
        # Append the maximum element seen so far to the result list
        rolling_max_elements.append(max_so_far)
    
    # Return the list of rolling maximum elements
    return rolling_max_elements


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It iterates over the input list, keeping track of the maximum element seen so far and appending it to the result list at each step. The function is then demonstrated with an example usage.