### Rolling Maximum Problem Solver
#### Python Implementation

```markdown
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
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num >= current_max:
            current_max = num
            rolling_max_list.append(current_max)
        else:
            rolling_max_list.append(current_max)

    return rolling_max_list

### Example Use Case
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function uses a simple iterative approach to keep track of the current maximum element as it iterates through the input list.

The key insight is that the rolling maximum element at each position is either the current number if it's greater than the current maximum, or the current maximum element remains the same if the current number is smaller.

This approach ensures that the output list has the same length as the input list and contains the rolling maximum elements at each position.