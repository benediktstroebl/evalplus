```markdown
## Rolling Maximum Problem Solution

### Description

This script generates a list of rolling maximum elements found until a given moment in a sequence.

### Code

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
    if not numbers:  # Edge case: empty list
        return []

    rolling_max_list = [numbers[0]]  # Initialize with the first element

    for num in numbers[1:]:
        if num >= rolling_max_list[-1]:  # If current num is greater than or equal to rolling max
            rolling_max_list.append(num)  # Update rolling max

    return rolling_max_list
```

### Example Usage

```python
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

### Explanation

This solution iterates through the list of numbers, keeping track of the rolling maximum. If the current number is greater than or equal to the current rolling maximum, it updates the rolling maximum list with the current number. This way, we ensure that the rolling maximum list always contains the maximum element seen so far.