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

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    # Initialize result list with the first element of input list
    result = [numbers[0]]

    # Iterate over the rest of the input list
    for num in numbers[1:]:
        # If current number is greater than the last element in result, append current number
        # Otherwise append the last element in result
        result.append(max(num, result[-1]))

    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, we define a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list, and for each number, it checks if it's greater than the last element in the result list. If it is, it appends the current number to the result list; otherwise, it appends the last element in the result list. The function returns the result list.