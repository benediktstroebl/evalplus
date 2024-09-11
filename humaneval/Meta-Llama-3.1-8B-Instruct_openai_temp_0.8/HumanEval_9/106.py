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
    result = [numbers[0]]  # Initialize result with the first element
    for num in numbers[1:]:  # Iterate over the list starting from the second element
        result.append(max(result[-1], num))  # Update the result with the maximum of the last element and the current number
    return result

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines a function `rolling_max` that calculates the rolling maximum of a given list of integers. It initializes the `result` list with the first element of the input list, then iterates over the remaining elements, updating the `result` list with the maximum between the last element of the `result` list and the current number. The function returns the `result` list. The script includes a test case to demonstrate the function's usage.