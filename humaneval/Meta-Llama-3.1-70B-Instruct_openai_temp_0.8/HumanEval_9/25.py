### Rolling Maximum Python Script
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

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

    max_values = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_values.append(current_max)

    return max_values


if __name__ == "__main__":
    print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
    print(rolling_max([]))  # Output: []
    print(rolling_max([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
    print(rolling_max([1]))  # Output: [1]
```
This script defines the `rolling_max` function, which iterates over the input list and keeps track of the current maximum value. It appends the current maximum value to the `max_values` list at each step. The function returns the `max_values` list, which represents the rolling maximum elements.

In the `if __name__ == "__main__":` block, there are example use cases that demonstrate the function's behavior with different input lists.