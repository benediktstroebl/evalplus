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
        raise ValueError("Input list cannot be empty.")

    max_so_far = current_max = numbers[0]

    result = [max_so_far]

    for num in numbers[1:]:
        current_max = max(num, current_max)
        max_so_far = max(max_so_far, current_max)
        result.append(max_so_far)

    return result

# Testing the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This Python script defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The function iterates over the input list, keeping track of the maximum element seen so far (`max_so_far`) and the current maximum element (`current_max`). It appends `max_so_far` to the result list at each iteration. The function returns the result list after iterating over the entire input list. If the input list is empty, a `ValueError` is raised. The script includes a test case to demonstrate the function's behavior.