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

    result = [numbers[0]]
    max_found = numbers[0]

    for num in numbers[1:]:
        if num >= max_found:
            max_found = num
            result.append(num)
        else:
            result.append(max_found)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([]))  # Output: []
print(rolling_max([5]))  # Output: [5]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list where each element is the maximum of all numbers up to and including the previous element in the original list. It uses a simple iteration to keep track of the maximum element found so far and append it to the result list whenever a new maximum is found. If no list is provided, it returns an empty list.