Here is the Python script that solves the problem in a markdown code block:

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
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script works by iterating through the input list of numbers, keeping track of the maximum number seen so far (`max_so_far`). It appends this maximum number to the result list at each step. This way, we can get the rolling maximum elements for the entire list.