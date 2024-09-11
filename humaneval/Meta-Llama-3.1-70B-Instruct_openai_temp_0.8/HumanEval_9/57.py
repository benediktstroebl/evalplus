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
    rolling_max_list = [max_so_far]
    
    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        rolling_max_list.append(max_so_far)
    
    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
print(rolling_max([1, 1, 1, 1, 1]))  # Output: [1, 1, 1, 1, 1]
print(rolling_max([]))  # Output: []
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes the maximum so far with the first element of the list and then iterates over the rest of the list, updating the maximum so far and appending it to the result list at each step. The function also includes a simple test suite to demonstrate its usage and correctness.