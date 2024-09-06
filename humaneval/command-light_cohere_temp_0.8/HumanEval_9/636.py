```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment
    in the sequence.
    :return [list of maxima(numbers,window=1,exclusive=False)
    """
    return [maxima(numbers, window=1, exclusive=False) for maxima in maximas(numbers, window=1, exclusive=False)]

def maximas(numbers: List[int], window: int, exclusive: bool) -> List[int]:
    if exclusive:
        return [num for num in numbers if num == numbers[window][0]]
    else:
        return [num for num in numbers if num != numbers[window][0] and num >= numbers[window][0]]
```
This solution solves the problem of finding the rolling maximum elements in a given list. It utilizes a Generate an list of all possible rolling maximum elements (with window size 1), and then filter the list to remove duplicates and keep only the maximum elements.