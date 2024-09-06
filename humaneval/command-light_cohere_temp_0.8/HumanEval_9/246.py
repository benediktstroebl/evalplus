```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling max elements found until a given moment in the sequence.
    Return a list of integers, where each integer is the maximum of the rolling window
    up to the given moment.
    >>> [2, 4, 2, 8, 3, 6] == rolling_max([1, 2, 3, 2, 3, 4, 2])
    """
    window = [num for num in numbers] + [numbers[-1]]
    rolling_window = [num for num in window if num > max_roll]
    max_roll = max(rolling_window)
    return [max_roll] + rolling_window[1:]
```