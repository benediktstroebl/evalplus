```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([4,1,3,2,5,9,3])
    [9,7,6,5,4]
    """
    return [x for x,i in enumerate(numbers)][::-1 :: i+1]
```