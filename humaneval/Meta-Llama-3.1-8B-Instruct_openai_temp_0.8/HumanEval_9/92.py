```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum
    max_list = []
    
    # Initialize the maximum value to negative infinity
    max_val = float('-inf')
    
    # Iterate over the input list
    for num in numbers:
        # If the current number is greater than the max_val, update max_val
        if num > max_val:
            max_val = num
        # Append the max_val to the list
        max_list.append(max_val)
    
    # Return the list of rolling maximum
    return max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```