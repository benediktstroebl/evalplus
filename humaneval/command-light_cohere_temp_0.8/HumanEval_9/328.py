```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling maximum elements found until a given moment in the sequence.
    :return [sorted(numbers, reverse=True)[:-i] for i in range(1, len(numbers)+1)]"""
    return sorted(numbers, reverse=True)[:-i] for i in range(1, len(numbers)+1)
```