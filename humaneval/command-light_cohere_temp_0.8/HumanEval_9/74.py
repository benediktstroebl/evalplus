```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers.append(max(numbers[1:], keep=numbers[0]))
    return numbers
```