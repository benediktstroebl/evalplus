```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    Test cases:
    1. All elements elements positive maxima elements should be equal, and the list should be empty.
    2. The first element is should be equal to any other, and not implement rolling max logic.
    """
    general case:
    rolling_max([1, 2, 2, 3, 2, 4])
    [2, 3, 4]
    """
    return [num for num in numbers if num > max_seen and max_seen == num]

#Test cases
rolling_max([1, 2, 3, 2, 3])
rolling_max([1, 2, 2, 3, 4, 2])
rolling_max([1, 2, 3, 4, 5])
rolling_max([1, 2, 3, 2, 6, 7])
rolling_max([])
rolling_max([10, 20, 30])
```