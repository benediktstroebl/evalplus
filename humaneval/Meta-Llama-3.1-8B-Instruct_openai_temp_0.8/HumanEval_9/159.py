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
    current_max = float('-inf')
    
    for num in numbers:
        if num > current_max:
            current_max = num
        result.append(current_max)
    
    return result


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

This script defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. It iterates over each number in the list, updating the current maximum if the current number is greater. The updated current maximum is then appended to the result list.

Note that the initial current maximum is set to negative infinity, so the first number in the list will always be added to the result.