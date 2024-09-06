```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until a given moment in the sequence.
    : The maximum value is calculated using a custom rolling window
    """
    return [x if (i == len(numbers) - 1) else numbers[-1] for i, x in enumerate(numbers, 1)]
```