```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until a given moment in the sequence.
    Args:
    numbers (List[int]): sequence of numbers
    Returns:
    List[int]: sequence of rolling maximum elements
    """
    # Initialize a list to store the rolling maximum elements and current index
    rolling_maxes = [None] * len(numbers)
    rolling_maxes[0] = numbers[0]

    # Move through the sequence and update the rolling maximum
    for i in range(1, len(numbers)):
        rolling_maxes[i] = max(rolling_maxes[i - 1], numbers[i])

    return rolling_maxes
``` 
Do you need anything else?