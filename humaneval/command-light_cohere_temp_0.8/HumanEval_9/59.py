```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Return a list of rolling max elements found until the moment provided in the sequence.
    """
    return [numbers[-2:] 
    """
    return [x for x in numbers[-2:]][::-1]
```