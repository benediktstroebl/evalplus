### Rolling Maximum Problem Solver
#### Overview
This script uses a Python list comprehension to generate a rolling maximum for a given sequence.

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
    return [max(numbers[:i+1]) for i in range(len(numbers))]

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```
#### Explanation
The provided function `rolling_max` takes a list of integers `numbers` and returns a list of rolling maximum elements. It uses a list comprehension to iterate over the input list, where `max(numbers[:i+1])` finds the maximum element up to the current index `i`. This rolling maximum is then appended to the result list.

Note: This approach has a time complexity of O(n^2) due to the use of `max(numbers[:i+1])`. For large inputs, a more efficient approach would be to maintain a running maximum through a single pass of the input list, resulting in a time complexity of O(n).