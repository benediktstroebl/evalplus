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
    if not numbers:
        return []

    result = [numbers[0]]
    max_until_now = numbers[0]

    for num in numbers[1:]:
        if num >= max_until_now:
            max_until_now = num
            result.append(num)
        else:
            result.append(max_until_now)

    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum value seen so far in the input list up to that point. The function uses a simple iterative approach to keep track of the maximum value seen so far and the corresponding element in the output list. The test case at the end demonstrates the function's correctness.