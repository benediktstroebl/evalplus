Here's a self-contained Python function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from the given list of integers.
    Args:
        numbers: list of integers
    Returns: list of integers, the rolling maximum elements
    """
    numbers = [num for num in numbers if num != float('-inf')]  # Filter out float('-inf')]
    result = [float('-inf')] + [num for num in numbers if num != float('-inf')]  # Initialize with -inf and then push current maximum
    while True:
        current_max = max(result[-1:])  # Calculate the current maximum value and update the tail
        result.append = (current_max if current_max > num else num)  # Compare the current number with the current maximum, and update the list accordingly
    return result
```
This script defines a function `rolling_max`, which takes a list of integers as an argument and returns a list of integers, representing the rolling maximum elements found in the input list.