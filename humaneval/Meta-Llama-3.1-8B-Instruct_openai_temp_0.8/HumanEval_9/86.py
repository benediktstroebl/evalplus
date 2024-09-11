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
    
    rolling_max_list = [numbers[0]]
    
    for num in numbers[1:]:
        if num >= rolling_max_list[-1]:
            rolling_max_list.append(num)
        else:
            rolling_max_list.append(rolling_max_list[-1])
    
    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function works by iterating over the input list, keeping track of the maximum element seen so far. Whenever a new maximum element is found, it is added to the `rolling_max_list`. Otherwise, the last maximum element is appended to the list. The function handles the case where the input list is empty and returns an empty list in this case.