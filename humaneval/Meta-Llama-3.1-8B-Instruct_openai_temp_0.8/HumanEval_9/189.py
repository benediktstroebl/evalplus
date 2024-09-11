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
        max_so_far = max(num, max_so_far)
        result.append(max_so_far)
    
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum of all elements in the input list up to that point. It uses a simple iterative approach to keep track of the maximum element seen so far and appends it to the result list. The function is tested with the provided example.