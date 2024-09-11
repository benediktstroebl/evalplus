```markdown
### Rolling Maximum Problem

#### Problem Statement

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
    List[int]: A list containing rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    result = [max_so_far]

    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result
```

#### Example Use Case

```python
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list containing the rolling maximum elements. The function iterates over the input list, keeping track of the maximum element seen so far. It appends the maximum element to the result list for each iteration.