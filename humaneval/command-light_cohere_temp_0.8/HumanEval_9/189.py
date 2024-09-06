```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_maxes: List[int] = [num for num in numbers if num > 0]  # Initialize with positive numbers

    for i in range(len(numbers)):
        while rolling_maxes and numbers[i] > rolling_maxes[-1]:
            rolling_maxes.pop(numbers[i])  # Pop the largest element from rolling maxes and move it to the front
        rolling_maxes.append(numbers[i])

    return rolling_maxes  # Return the list of rolling maxima
```