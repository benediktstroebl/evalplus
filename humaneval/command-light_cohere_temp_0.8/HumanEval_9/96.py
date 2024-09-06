```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize the rolling window
    max_element = numbers[0]
    rolling_window = [max_element]

    # Iterate through the list
    for num in numbers[1:]:
        # Calculate the current maximum element
        current_max = max(rolling_window[-1], num)

        # Update the rolling window
        rolling_window.append(current_max)
        max_element = current_max

    return rolling_window
```