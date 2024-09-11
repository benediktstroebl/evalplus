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
    result = []
    current_max = float('-inf')
    
    for num in numbers:
        if num >= current_max:
            current_max = num
        result.append(current_max)
    
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a variable `current_max` to keep track of the maximum element encountered so far, and appends this value to the result list whenever a new maximum is found. The function then returns the result list.