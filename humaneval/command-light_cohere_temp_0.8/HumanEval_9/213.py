```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements found until a given moment
    in the sequence, using an efficient sliding window approach.

    Args:
        numbers (List[int]): Sequence of integers.
    Returns: List[int]: List of rolling maximum elements.
    """

rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
```