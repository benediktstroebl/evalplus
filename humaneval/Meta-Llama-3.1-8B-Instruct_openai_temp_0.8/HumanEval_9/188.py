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
    max_seen = float('-inf')  # Initialize max_seen as negative infinity
    result = []  # Initialize an empty list to store the result

    for num in numbers:
        # If the current number is greater than max_seen, update max_seen
        if num > max_seen:
            max_seen = num
        # Append the maximum seen so far to the result list
        result.append(max_seen)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum element found until the given moment in the sequence. It iterates through the input list, updating the `max_seen` variable whenever it encounters a number greater than the current `max_seen`. The `max_seen` value is then appended to the `result` list, which is returned at the end of the function. The script includes a test case to demonstrate the function's usage.