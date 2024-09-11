```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum element found until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(max(numbers[:i+1]))
    
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines the `rolling_max` function that takes a list of integers as input and returns a list of rolling maximum element found until given moment in the sequence. It first checks if the input list is empty. If it is, the function returns an empty list. Otherwise, it initializes the result list with the first element of the input list. Then it iterates over the input list starting from the second element (index 1). For each element, it appends the maximum of all elements found until the current position to the result list. Finally, it returns the result list. The script includes a test case to demonstrate the function's usage.