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
    # Initialize an empty list to store the rolling maximum elements
    max_elements = []
    
    # Initialize the maximum element found so far as negative infinity
    max_found = float('-inf')
    
    # Iterate over the input list
    for num in numbers:
        # Update the maximum element found so far if the current number is greater
        if num > max_found:
            max_found = num
        
        # Append the maximum element found so far to the result list
        max_elements.append(max_found)
    
    # Return the list of rolling maximum elements
    return max_elements

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function called `rolling_max` that calculates the rolling maximum elements from a given list of integers. The function uses a simple iterative approach to find the maximum element found so far at each step and appends it to the result list. The script also includes a test case to demonstrate the function's correctness.