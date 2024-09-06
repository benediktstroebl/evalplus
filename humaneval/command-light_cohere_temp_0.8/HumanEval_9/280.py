Here's a self-contained Python function that solves the markdown-code block problem:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements in a given list of integers.
    Parameters: numbers - list of integers
    Returns:  list of integers - rolling maximum elements.
    """
    `numbers`: list of integers
    `current_index`: int - current index
    `window_size`: int - window size
    """
    numbers: List[int] = [1, 2, 3, 2, 3, 4, 2]
    current_index = 0
    window_size = 2

    # Initialize the list with the initial maximum element
    rolling_max = [numbers[current_index]]

    # Move the index and check for the end of the list
    while current_index < len(numbers) - window_size:
        current_index += 1
        # Get the current element and add it to the rolling maximum
        rolling_max.append(numbers[current_index])
        
        # Check if the rolling maximum element is greater than the current maximum element
        if rolling_max[-1] > numbers[current_index]:
            rolling_max = [numbers[current_index]]

    return rolling_max
```
This code defines a function called rolling_max that takes a list of integers as input and returns a new list of integers - the rolling maximum elements found up to the given list of integers, following the algorithm explained in the comments.