### Rolling Maximum Function
#### Returns a list of rolling maximum elements found until a given moment in the sequence.

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
    max_until_now = float('-inf')  # Initialize max_until_now as negative infinity
    result = []  # Initialize an empty list to store the result

    for num in numbers:
        if num >= max_until_now:  # If current number is greater than or equal to max_until_now
            max_until_now = num  # Update max_until_now
            result.append(num)  # Append max_until_now to the result list
        else:
            result.append(max_until_now)  # Append max_until_now to the result list

    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
# Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a single pass through the input list, keeping track of the maximum element seen so far (`max_until_now`). If the current number is greater than or equal to `max_until_now`, it updates `max_until_now` and appends it to the result list. Otherwise, it appends the current `max_until_now` to the result list. The function returns the result list after processing all numbers in the input list.