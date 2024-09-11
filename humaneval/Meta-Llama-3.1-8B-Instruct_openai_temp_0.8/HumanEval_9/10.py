### Rolling Maximum Problem Solution
#### Problem Description
From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

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
    for num in numbers[1:]:
        if num >= result[-1]:
            result.append(num)
        else:
            result.append(result[-1])

    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 4, 3, 2, 1]))  # [5, 5, 5, 5, 5]
print(rolling_max([]))  # []
```
This solution initializes the result list with the first element of the input list. Then, it iterates over the rest of the input list. If a number is greater than or equal to the current maximum, it updates the maximum. If a number is less than the current maximum, it keeps the current maximum. This way, it keeps track of the rolling maximum at each step.