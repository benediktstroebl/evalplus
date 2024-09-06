```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in the given list of integers
    >
    <start> :< end > = [max(n, m) for n, m in zip(numbers[::start], numbers[end:])]
    >
    [start, end, rolling_max([10, 3, 1, 9, 2, 7, 5, 4, 3, 2, 1])]
    """
    start, end = 0, len(numbers) - 1
    return [start, end, max(numbers[start:end], numbers[start])]
```