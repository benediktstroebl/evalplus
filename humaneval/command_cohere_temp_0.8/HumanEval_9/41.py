```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.
    
    Args:
        numbers (List[int]): The list of integers to be processed.
        rolling_window (int): The size of the rolling window to look at to find the maximum.
    
    Returns:
        List[int]: A list of the maximum integers at each step of the rolling window.
    """
    if not numbers:
        return []

    return [max(numbers[i:i+rolling_window]) for i in range(len(numbers) - rolling_window + 1)]

# Tests:
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3

print(rolling_max(numbers, rolling_window))  # [1, 2, 3, 3, 3, 4, 4]
```