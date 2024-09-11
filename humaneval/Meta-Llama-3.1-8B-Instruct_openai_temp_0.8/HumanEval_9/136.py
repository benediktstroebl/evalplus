### Rolling Maximum
#### Self-Contained Python Script

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
    max_so_far = float('-inf')
    
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple and efficient approach to find the rolling maximum of a given list of integers. It maintains a `max_so_far` variable to keep track of the maximum number seen so far and appends this value to the result list at each step. This way, it generates a list of rolling maximum elements found until the given moment in the sequence.