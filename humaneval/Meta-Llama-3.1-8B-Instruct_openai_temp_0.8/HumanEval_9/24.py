### Rolling Maximum Script
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

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

### Explanation
This script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the rolling maximum elements. It maintains a variable `max_so_far` to keep track of the maximum element seen so far and a list `result` to store the rolling maximum elements. It iterates over the input list, updating `max_so_far` and appending it to `result` for each element. The function returns `result`.

The example usage at the end demonstrates how to use the `rolling_max` function with a sample list of numbers.