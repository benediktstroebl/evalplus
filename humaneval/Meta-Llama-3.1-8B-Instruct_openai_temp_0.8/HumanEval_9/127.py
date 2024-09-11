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
    
    max_so_far = numbers[0]
    result = [max_so_far]
    
    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    
    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum number seen so far in the input list. The function uses a variable `max_so_far` to keep track of the maximum number seen so far, and it appends the updated `max_so_far` to the result list at each iteration. The result list is returned at the end of the function.

The script also includes a docstring that provides a description of the function, explains its parameters and return value, and includes an example usage of the function. Finally, the script includes a call to the `rolling_max` function with an example input list and prints the result.