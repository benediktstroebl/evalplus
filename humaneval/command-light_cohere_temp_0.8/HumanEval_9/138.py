```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in the given list
    >>> rolling_max([1, 2, 3, 4, 3, 5])
    [3, 4, 5]
    """
    max_window = [x for x in numbers[-1: :: }]
    rolling_max_elements = [x for x in numbers[-1:: >> 1]] + [max_window]
    return rolling_max_elements

rolling_max([1, 2, 3, 4, 3, 5]) # [3, 4, 5]
```