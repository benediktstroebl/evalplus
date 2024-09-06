```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [num for num, index in sorted((num, index), reverse=True) for index in range(len(numbers) - 1)]
```
The function uses the sorted function with a reverse=True argument and a tuple ((num, index),) as the sorting key. The sorted function then returns a list of tuples in sorted order, which can be converted to a list of numbers using the list() function.