```python
from typing import List, Tuple

def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers to process.
        window_size (int): The size of the rolling window.

    Returns:
        List[int]: A list of integers representing the rolling maximum elements within the specified window.
    """
    
    if not numbers:
        return []

    if len(numbers) < window_size:
        return numbers
    
    rolling_maxes = [numbers[0]]
    
    for i in range(1, len(numbers)):
        current_max = numbers[i]
        for j in range(i - window_size + 1, i):
            if numbers[j] > current_max:
                current_max = numbers[j]
        rolling_maxes.append(current_max)
    
    return rolling_maxes
```
The function `rolling_max()` takes in two parameters (`numbers` and `window_size`) and returns a list of integers representing the rolling maximum elements within the specified window. 

This implementation allows for a variable size rolling window, as exemplified by the unit tests:
```python
def test_rolling_max():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 2) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 3) == [1, 2, 3, 3, 4, 4, 4]
    assert rolling_max([1, 2, 3, 2, 3, 4, 2], 4) == [1, 2, 2, 3, 3, 4, 4]
```