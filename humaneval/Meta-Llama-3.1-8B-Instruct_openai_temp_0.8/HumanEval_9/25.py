### Rolling Maximum Element
#### Problem Description
From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution
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
    
    max_so_far = numbers[0]
    result = [max_so_far]
    
    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
        result.append(max_so_far)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script uses a simple iterative approach to keep track of the maximum element seen so far and appends it to the result list at each step. The function returns the list of rolling maximum elements.