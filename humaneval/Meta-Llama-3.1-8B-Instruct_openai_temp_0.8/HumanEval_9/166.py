```markdown
### Rolling Maximum Problem
#### Problem Description
From a given list of integers, generate a list of rolling maximum element found until given moment
in the sequence.

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
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')
    result = []
    
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation
The `rolling_max` function takes a list of integers as input and returns a list of rolling maximum elements.
The function uses a variable `max_so_far` to keep track of the maximum element seen so far.
For each number in the input list, it updates `max_so_far` if the current number is greater than `max_so_far`.
Finally, it appends `max_so_far` to the result list.