### Rolling Maximum Calculator
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
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    current_max = float('-inf')

    for num in numbers:
        if num >= current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

### Explanation

This script defines a function `rolling_max` that calculates the rolling maximum of a given list of integers. It initializes an empty list `rolling_max_list` to store the result and a variable `current_max` to keep track of the maximum element encountered so far. The function iterates through the input list, and for each number, it checks if it's greater than or equal to the current maximum. If it is, it updates the `current_max` variable. The function then appends the current maximum to the `rolling_max_list`. Finally, it returns the `rolling_max_list`. The example usage demonstrates how to use the function with a sample input list.