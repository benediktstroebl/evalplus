```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([5,2,3])
    [5]
    >>> rolling_max([6,'44','22','23','12','44'])
    ['44']
    """
    # remove the first element because the rolling starts from the next number
    numbers.remove(0)
    rolling_max = [x for x in numbers]
    rolling_max = [x for x, i in zip(numbers, range(len(numbers)+1)) if i < len(numbers)]
    rolling_max.remove(0)
    rolling_max.append(numbers[0])
    rolling_max.remove(0)
    rolling_max
    return rolling_max
```