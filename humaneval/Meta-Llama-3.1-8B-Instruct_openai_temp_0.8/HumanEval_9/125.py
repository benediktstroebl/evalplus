```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.
    
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

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the `rolling_max_list` with the first element of the input list and then iterates through the rest of the list. If the current number is greater than or equal to the last element in the `rolling_max_list`, it appends the current number to the list. Otherwise, it appends the last element in the `rolling_max_list`. Finally, it returns the `rolling_max_list`. The script also includes a test case to demonstrate the function's usage.