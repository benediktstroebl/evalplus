```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Returns the list of rolling maximum elements found until a given moment 
    in the sequence.
    Args:
        list of integers
    Returns:
        list of integers, with the maximum element rolling. 
    """
    uses list comprehension to generate a list of rolling max elements, 
    and type hints to make it much easier to read. 
"""
    # Initialize a list to store rolling max elements.
    rolling_maxes = []

    # Initialize a counter for the index of the current maximum element.
    current_index = 0

    # Loop through the list of numbers until the counter exceeds the index of the moment to keep.
    for number in numbers:
        # Set the current maximum element to the number.
        current_max = number

        # If the counter is greater than the current index, increment it.
        current_index += 1

        # If the current maximum element is greater than the last element in the list, append it to the list.
        rolling_maxes.append(current_max)

    # Return the list of rolling max elements.
    return rolling_maxes
```