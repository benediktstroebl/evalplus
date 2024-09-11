Here is the Python script that solves the problem:

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    rolling_max = float('-inf')
    
    for num in numbers:
        if num >= rolling_max:
            rolling_max = num
        rolling_max_list.append(rolling_max)
        
    return rolling_max_list
```

This script uses a simple method to find the rolling maximum. It initializes a variable `rolling_max` to negative infinity, and then iterates through the input list. If it encounters a number that is greater than or equal to the current `rolling_max`, it updates `rolling_max` to that number. It then appends the current `rolling_max` to the `rolling_max_list`. At the end of the iteration, it returns the `rolling_max_list`.