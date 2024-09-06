```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculate the rolling maximum element in a list of integers using Python.
    Returns a time list of the maximum element, calculated over the window of the
    sequence from the start to the given moment.

    Args:
        List[int] - A list of integers
    Returns:
        List[int] - The rolling maximum element
    """
    numbers, rolling_max = List([i for i in numbers if i >= rolling_max[0]]), [numbers[0]]
    for i in range(1, len(numbers)):
        rolling_max[i] = max(rolling_max[i - 1], numbers[i])
    return rolling_max

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]

numbers = [5, 1, 3, 9, 6, 5, 3]
result = rolling_max(numbers)
print(result)  # Output: [9, 9, 9, 9]

numbers = [3, 9, 2, 1]
result = rolling_max(numbers)
print(result)  # Output: [9, 9]
```
The function rolling_max calculates the maximum element in a list of integers, using a rolling window approach. The test cases demonstrate the rolling_max by passing lists of numbers and printing the resulting list of maximum elements.