```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling max elements found until a given moment
    in the sequence.
    Return a list of maximum elements which are the first n elements of the list
    """
    return [n for n, idx in reversed(sorted(numbers)) for idx in range(1, n)]
```
Do you have any other questions about Python, data structures, or other related topics?