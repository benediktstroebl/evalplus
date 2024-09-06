```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling 
    maximum elements found until the given moment in the 
    sequence.
    Test cases are
    each of the possible moment, and passes the 
    corresponding test
    """
    return [n for n, _ in zip(numbers[numbers.index()], numbers[2])
```