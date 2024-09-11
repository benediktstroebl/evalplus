```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers: A list of integers

    Returns:
    A list of rolling maximum elements

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    max_found = float('-inf')  # Initialize max_found as negative infinity

    for num in numbers:
        if num >= max_found:
            max_found = num
        rolling_max_list.append(max_found)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found until each moment in the sequence. The function uses a simple iterative approach to maintain the maximum found so far and append it to the result list at each step. The example usage demonstrates how to call the function with a sample list of numbers and print the result.