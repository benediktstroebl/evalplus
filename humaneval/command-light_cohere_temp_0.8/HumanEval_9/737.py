```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements in the given list of integers.
    The rolling maximum elements are the maximum elements found in the sequence, 
    starting from the first element and rolling over to the next occurrences.
    >>> [1, 2, 3, 2, 3, 4, 2]
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x, _ in zip(numbers[:-len(numbers) // 2], numbers[::2])]
```