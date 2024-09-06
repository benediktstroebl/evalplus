```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    This function takes a list of integers and returns the list of 
    rolling maximum elements found until a given moment 
    in the sequence.
    """ 
    A rolling maximum element is defined as the maximum of a window of elements 
    starting from the index 0. 
    The window size is determined by the parameter window.
    """ 
    numbers = [1, 2, 3, 2, 3, 4, 2]
    window = 1 
    rolling_maxes = [numbers[0]]
    while window <= len(numbers) - 1:
        current = numbers[window]
        window += 1
        new_max = current
        for i in range(window, len(numbers)):
            current = numbers[i]
            if current > new_max:
                new_max = current
        rolling_maxes.append(new_max)
    return rolling_maxes
```