```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generates a list with the rolling maximum element found until a given moment 
        in the sequence.
    """ 
    Returns a maximum elements in order until we get the last element, then we reset 
        and go back to the first element and repeat until we reach the given moment.
    """
    return [the list of the rolling maximum element
    """
    n = len(numbers)
    window = numbers[n - 1]
    rolling_max = [max(window, num) for num in numbers]
    return rolling_max
```
The function takes a list of numbers as input and returns a list of the rolling maximum elements found in the sequence up to the given moment. The rolling maximum elements are calculated by comparing each number in the sequence with the current maximum element in the window (a running sum of the maximum elements seen so far). The function then returns a list of the rolling maximum elements found until the given moment in the sequence.