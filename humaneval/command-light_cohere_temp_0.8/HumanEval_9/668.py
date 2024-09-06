```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of the rolling maximum element found in the sequence.
    Each element in the max sequence is accessed 
    twice to get the maximum of the two values and 
    store it.
    Returns the max of the sequence until the list is empty.
"""
    # Initialize a list of rolling maximum elements
    rolling_maxes = [0]

    # Iterate over the sequence of numbers
    for num in numbers:
        # Calculate the maximum of the current number and the 
        # last element in the rolling max sequence
        current_max = num
        max_element = rolling_maxes[-1]
        rolling_maxes.append(max(current_max, max_element))

    # Return the list of rolling max elements
    return rolling_maxes
```