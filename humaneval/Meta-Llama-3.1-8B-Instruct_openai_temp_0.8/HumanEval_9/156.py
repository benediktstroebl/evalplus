### Rolling Maximum Elements
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

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation

This script defines a function `rolling_max` that calculates the rolling maximum elements from the given list of integers. It iterates over the list and keeps track of the maximum element found so far. The maximum element is appended to the result list at each step. If the current number is greater than or equal to the maximum element found so far, it updates the maximum element. This way, the function generates the list of rolling maximum elements efficiently.