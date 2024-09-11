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
    if not numbers:
        return []
    
    result = [numbers[0]]
    max_so_far = numbers[0]
    
    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
        result.append(max_so_far)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum value seen so far in the original list. It uses a simple iterative approach to keep track of the maximum value seen so far and appends it to the result list at each step. If the input list is empty, it returns an empty list as well. The example usage at the end demonstrates how to use this function to find the rolling maximum of a given list of numbers.