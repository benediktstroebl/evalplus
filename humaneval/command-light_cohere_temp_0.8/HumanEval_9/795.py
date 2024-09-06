```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    : Return a list of maximum elements in order of occurrence.
    """
    Each value in the list is either the maximum found so far, or the current number if no better max is found.
    """

test_rolling_max_example = [3, 2, 4, 1, 5, 6, 3]
rolling_max(test_rolling_max_example)
print(rolling_max_example)
```