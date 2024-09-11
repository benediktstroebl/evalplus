```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    Args:
        numbers (List[int]): A list of integers
    
    Returns:
        List[int]: A list of rolling maximum elements
    
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]
    
    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than the last element in the result list, append it
        if num > result[-1]:
            result.append(num)
        # Otherwise, append the last element in the result list
        else:
            result.append(result[-1])
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that calculates the rolling maximum of a given list of integers. It initializes the result list with the first element of the input list and then iterates over the rest of the list, appending the current number to the result list if it's greater than the last element in the list, or appending the last element in the list otherwise.