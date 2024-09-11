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
    maxs = []
    
    # Initialize the current maximum as negative infinity
    curr_max = float('-inf')
    
    # Iterate over each number in the input list
    for num in numbers:
        # If the current number is greater than the current maximum, update the current maximum
        if num > curr_max:
            curr_max = num
        
        # Append the current maximum to the list of maximums
        maxs.append(curr_max)
    
    # Return the list of maximums
    return maxs

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```