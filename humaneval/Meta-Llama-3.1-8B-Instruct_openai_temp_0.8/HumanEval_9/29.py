```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum element found until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    
    # Initialize the maximum value to negative infinity
    max_so_far = float('-inf')
    
    # Iterate over each number in the list
    for num in numbers:
        # If the current number is greater than max_so_far, update max_so_far
        if num > max_so_far:
            max_so_far = num
        
        # Append the current max_so_far to the result list
        result.append(max_so_far)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found until the given moment in the sequence. The function initializes the maximum value to negative infinity and then iterates over each number in the list. If the current number is greater than the maximum value, it updates the maximum value; then it appends the current maximum value to the result list. The function returns the result list, which contains the rolling maximum elements found until the given moment in the sequence.