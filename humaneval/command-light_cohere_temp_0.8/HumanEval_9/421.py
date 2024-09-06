```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in the given list
    >>> rolling_max([1, 2, 3, 4, 5])
    [3, 4, 5, 5]
    """
    numbers.append(max(numbers[-1:]))
    return numbers[:]
```