```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment in the sequence.
    :param numbers: list of integers
    :return: list of rolling maximum elements
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    rolling_maxes = [num for num in numbers if num == numbers[0]]
    for i in range(len(numbers) - 1):
        rolling_maxes.append(max(numbers[i+1:]))
    return rolling_maxes
```