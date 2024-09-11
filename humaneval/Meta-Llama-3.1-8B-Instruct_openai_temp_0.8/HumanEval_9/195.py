**Rolling Maximum Function in Python**
=====================================

Here is a Python script that defines a function `rolling_max` to calculate the rolling maximum of a given list of integers.

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

    max_num = numbers[0]
    result = [max_num]

    for num in numbers[1:]:
        max_num = max(max_num, num)
        result.append(max_num)

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which initializes the maximum element and the result list with the first element of the input list. Then, it iterates through the rest of the list, updating the maximum element and appending it to the result list. If the input list is empty, the function returns an empty list.