### Rolling Maximum Problem
#### Python Solution

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

In this script, we initialize the `max_so_far` variable to negative infinity and iterate over the input list. We update `max_so_far` with the maximum between its current value and the current number. We then append `max_so_far` to the result list. The result list now contains the rolling maximum elements.