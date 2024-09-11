```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment 
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(max(numbers[:i+1]))
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a list `result` to store the rolling maximum elements. It initializes `result` with the first element of `numbers`, then iterates over the rest of the elements in `numbers`. For each element, it finds the maximum of all elements before (and including) the current position, and appends this maximum to `result`. Finally, it returns `result`. The script includes a test case to demonstrate the function's behavior.