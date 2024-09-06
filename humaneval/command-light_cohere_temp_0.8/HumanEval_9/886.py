```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from the given list.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elements = []
    while True:
        current_max = max(numbers)
        max_elements.append(current_max)
        numbers.remove(current_max)
        if len(numbers) == 0:
            break
    return max_elements
```