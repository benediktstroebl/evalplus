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
            result.append(num)
            max_so_far = num
        else:
            result.append(max_so_far)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that calculates the rolling maximum of a given list of integers. It iterates over the list, keeping track of the maximum value seen so far. Whenever it encounters a number that is greater than or equal to the current maximum, it updates the maximum and appends the new maximum to the result list. Otherwise, it appends the current maximum to the result list. The function handles an empty list as an edge case, returning an empty list in this case.