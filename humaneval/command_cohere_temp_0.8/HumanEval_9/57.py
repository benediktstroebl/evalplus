```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    
    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The size of the rolling maximum window.
    
    Returns:
        List[int]: A list of integers representing the rolling maximum elements found at each position.
    """
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('-inf')] * rolling_window

    max_window = [numbers[0]]
    current_max = numbers[0]

    for i in range(1, len(numbers)):
        current_max = max(numbers[i], current_max)
        max_window.append(current_max)

        if i >= rolling_window:
            current_max = max(max_window[-rolling_window:])
            max_window = max_window[-rolling_window:] + [current_max]

    return max_window
```

The `rolling_max` function takes two parameters: a `numbers` list of integers and a `rolling_window` specifying the size of the rolling maximum window.

The function handles edge cases where an empty list or a window size larger than the list length is provided.

It then constructs a rolling maximum window, updating it with each element in the input list. The resulting list is returned, containing the rolling maximum elements at each position.