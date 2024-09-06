```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the moment specified.
    >>> [1, 2, 3, 4] is the test moment
    """
    return [n for n,i in zip(numbers[:i], numbers[i+1:]) for i in range(len(numbers))]
```