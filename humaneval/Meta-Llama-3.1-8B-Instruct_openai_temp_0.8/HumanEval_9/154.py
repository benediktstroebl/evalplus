```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers

    Returns:
    List[int]: A list of rolling maximum elements

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    result = [max_so_far]

    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script uses a simple iterative approach to find the rolling maximum. It initializes `max_so_far` with the first element of the list and `result` with a list containing `max_so_far`. Then, for each element in the list, it checks if the current element is greater than or equal to `max_so_far`. If it is, `max_so_far` is updated to the current element. The rolling maximum is then appended to `result`. Finally, the function returns `result`.