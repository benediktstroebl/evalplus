```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers

    Returns:
        A list of rolling maximum element found until given moment in the sequence

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = [max(numbers[:i+1]) for i in range(len(numbers))]
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses list comprehension with `max` function to generate the rolling maximum list. The script also includes a test case to demonstrate the function's usage. 

In the provided example, for each index `i` in the input list, it calculates the maximum element found so far in the sequence up to the `i-th` index, and stores it in the `result` list. The final `result` list contains the rolling maximum elements for each index in the input list.