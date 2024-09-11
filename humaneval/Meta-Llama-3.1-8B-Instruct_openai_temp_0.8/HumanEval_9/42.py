Here's a Python script that solves the problem using a simple and efficient approach:

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
    if not numbers:
        return []

    max_so_far = numbers[0]
    result = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

In this script, we first initialize `max_so_far` with the first element of the input list and append it to the result list. Then we iterate over the rest of the list, keeping track of the maximum element seen so far (`max_so_far`). At each step, we update `max_so_far` if we encounter a larger number, and then append `max_so_far` to the result list. This way, we efficiently keep track of the rolling maximum element in the sequence.