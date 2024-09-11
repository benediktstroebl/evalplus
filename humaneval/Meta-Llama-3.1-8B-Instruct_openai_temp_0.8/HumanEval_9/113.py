### Rolling Maximum Problem Solution
#### Description
This script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the rolling maximum element found until that moment in the sequence.

#### Code
```markdown
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
    result = []
    max_so_far = float('-inf')

    for num in numbers:
        max_so_far = max(num, max_so_far)
        result.append(max_so_far)

    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```

#### Explanation
The `rolling_max` function initializes an empty list `result` to store the rolling maximum elements and a variable `max_so_far` to keep track of the maximum element seen so far. It then iterates over the input list, updating `max_so_far` to be the maximum of the current number and `max_so_far`, and appending `max_so_far` to the `result` list. Finally, it returns the `result` list.