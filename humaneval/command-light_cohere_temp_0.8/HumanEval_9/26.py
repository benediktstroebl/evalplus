```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A utility function that returns the rolling maximum element in a given list of integers.
    Args:
        numbers (List[int]): a list of integers
    Returns:
        List[int]: list of rolling maximum elements found in the sequence
    """
    # Initialize the rolling maximum list
    rolling_max = [num for num in numbers]

    # Calculate the rolling maximum and add to the list
    for num in numbers[1:]:
        rolling_max.append(max(rolling_max, num))

    return rolling_max
``` 

This function takes a list of integers as input and returns a list of integers that are the rolling maximum elements in the sequence. It uses the maximum function to get the maximum value between the current element and the rolling maximum, and then appends the new maximum value to the rolling_max list.