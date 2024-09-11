```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements found in the sequence.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    current_max = float('-inf')
    
    for num in numbers:
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)
    
    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found in the sequence. It iterates over the input list, updating the `current_max` variable whenever it encounters a larger number. The `rolling_max_list` is built by appending the `current_max` to it at each step. Finally, the function returns the `rolling_max_list`.