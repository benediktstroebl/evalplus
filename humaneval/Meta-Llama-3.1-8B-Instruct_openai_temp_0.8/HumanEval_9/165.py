### Rolling Maximum Function
#### Python Script

```markdown
### Problem Statement
From a given list of integers, generate a list of rolling maximum element found until given moment
in the sequence.

### Code
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements found until the given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')
    result = []

    for number in numbers:
        max_so_far = max(max_so_far, number)
        result.append(max_so_far)

    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

### Explanation

This script defines a function called `rolling_max` that takes a list of integers as input.
It initializes `max_so_far` to negative infinity and an empty list `result` to store the rolling maximums.

The function then iterates over each number in the input list. For each number, it updates `max_so_far` to be the maximum of the current number and `max_so_far`. This is the key step in finding the rolling maximum.

Finally, it appends the current `max_so_far` to the `result` list. After iterating over all numbers, it returns the `result` list, which contains the rolling maximums found until each moment in the sequence.