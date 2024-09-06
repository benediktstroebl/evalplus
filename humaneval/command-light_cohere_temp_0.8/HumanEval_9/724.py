```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in the given list
    Each element of the list is an integer
    Returns the list of rolling max elements found until the given moment in the sequence
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x in numbers if x == numbers[-1] or max(numbers[:-len(numbers)-1])]
```