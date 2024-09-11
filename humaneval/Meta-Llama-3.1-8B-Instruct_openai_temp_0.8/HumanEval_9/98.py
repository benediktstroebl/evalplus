```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers

    Returns:
        A list of rolling maximum elements

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

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iterative approach to keep track of the maximum element seen so far, updating it whenever a larger element is encountered. The result is appended to the output list, which is returned at the end. The script also includes a test case to demonstrate the function's behavior.