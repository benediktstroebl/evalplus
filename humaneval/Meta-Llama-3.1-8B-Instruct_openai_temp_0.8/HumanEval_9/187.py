### Rolling Maximum Algorithm

The following Python script implements a function `rolling_max` that calculates the rolling maximum for a given list of integers.

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculate the rolling maximum for a given list of integers.

    Args:
    numbers: A list of integers.

    Returns:
    A list of rolling maximum elements found until the given moment.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_until_now = float('-inf')

    for num in numbers:
        if num > max_until_now:
            max_until_now = num
        result.append(max_until_now)

    return result
```

### Example Usage

```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]
print(rolling_max([1, 1, 1, 1, 1]))  # Output: [1, 1, 1, 1, 1]
```

This script uses a simple and efficient approach by maintaining a running maximum value (`max_until_now`) and updating it whenever a larger number is encountered. The result is a list of rolling maximum elements found until the given moment.