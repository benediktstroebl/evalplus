```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = []
    while True:
        current_max = max(numbers)
        max_numbers.append(current_max)
        numbers.remove(current_max)
        if len(numbers)==0:
            break
    return max_numbers
```