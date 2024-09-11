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
    """
    if not numbers:
        return []

    rolling_maximums = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_maximums.append(current_max)

    return rolling_maximums


# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([-1, -2, -3, -2, -3, -4, -2]))  # Output: [-1, -2, -3, -3, -3, -4, -4]
print(rolling_max([]))  # Output: []
print(rolling_max([5]))  # Output: [5]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It iterates over the input list, updating the current maximum whenever a larger number is encountered. The function returns a list where each element is the maximum of all elements up to that point in the input list. The script also includes example usage and test cases.