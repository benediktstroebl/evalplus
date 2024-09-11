### Rolling Maximums in a List
#### Python Script

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximums.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    current_max = float('-inf')  # Initialize current max to negative infinity

    for num in numbers:
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

This script defines a function `rolling_max` that takes a list of integers as input. It iterates over the list, keeping track of the maximum element encountered so far (`current_max`). It appends the current maximum to the output list (`rolling_max_list`) for each number in the input list. Finally, it returns the `rolling_max_list`, which contains the rolling maximums.

You can run this script to see the rolling maximums for the example list `[1, 2, 3, 2, 3, 4, 2]`.