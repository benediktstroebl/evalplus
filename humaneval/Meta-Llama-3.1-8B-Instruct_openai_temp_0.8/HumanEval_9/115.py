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
        raise ValueError("Input list is empty")

    rolling_max_list = []
    current_max = float('-inf')

    for num in numbers:
        if num > current_max:
            current_max = num
        rolling_max_list.append(current_max)

    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It initializes an empty list to store the rolling maximum elements and a variable `current_max` to keep track of the maximum element seen so far. It then iterates over the input list, updating `current_max` whenever a larger number is encountered and appending `current_max` to the `rolling_max_list`. Finally, it returns the `rolling_max_list`. The script also includes a test case to demonstrate the function's behavior.