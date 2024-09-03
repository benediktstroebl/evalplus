```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Find the maximum element in a list, and then add one and return the maximum again
    for each subsequent element.
    >>> numbers[n -> [x + 1 for x in numbers if x > numbers[-1]]
    """
    numbers.append(numbers[-1])
    return [x + 1 for x in numbers if x > numbers[-1]]
```