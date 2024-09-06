```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x, i in zip(numbers, numbers[1:]) if i == numbers[0]]
``` 
This code defines a function called rolling_max that takes a list of integers as input and returns a list of the rolling maximum elements found in the list up to the given moment.