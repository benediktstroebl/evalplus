### Rolling Maximum
#### Problem Statement
Given a list of integers, generate a list of rolling maximum element found until the given moment in the sequence.

#### Solution

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum element found until the given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')  # Initialize max_so_far to negative infinity
    result = []

    for num in numbers:
        # Update max_so_far if the current number is greater
        max_so_far = max(max_so_far, num)
        # Append max_so_far to the result list
        result.append(max_so_far)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found until the given moment in the sequence. The function uses a simple and efficient approach to keep track of the maximum element found so far and updates it whenever a larger number is encountered. The maximum element found so far is then appended to the result list. Finally, the function returns the result list.