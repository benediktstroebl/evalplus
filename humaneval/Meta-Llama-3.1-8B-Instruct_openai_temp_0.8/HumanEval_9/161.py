### Rolling Maximum in Python
#### Problem Description
Generate a list of rolling maximum element found until given moment in the sequence.

#### Code
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

    max_until_now = numbers[0]
    result = [max_until_now]

    for num in numbers[1:]:
        max_until_now = max(max_until_now, num)
        result.append(max_until_now)

    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
#### Explanation
This Python function `rolling_max` generates a list of rolling maximum elements from a given list of integers. It initializes the maximum element found until now as the first element of the list, and then iterates over the rest of the list, updating the maximum element found until now as it encounters larger numbers. The function returns the list of rolling maximum elements.