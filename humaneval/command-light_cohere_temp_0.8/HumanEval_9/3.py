```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    rolling_max([1, 2, 3, 4, 5]) -> [1, 2, 3, 4, 5]
    """
    max_window = []
    for num in numbers:
        if len(max_window) > 0 and num >= max_window[-1]:
            max_window.append(num)
        else:
            max_window.append(num)
        else:
            break
    return max_window
```