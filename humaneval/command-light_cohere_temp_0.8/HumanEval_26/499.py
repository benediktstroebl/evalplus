```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list and return the unique elements in order.
    Input:
    numbers = [1, 2, 3, 2, 4, 3, 4]
    Output: [1, 2, 3, 4]
    """
    return list(set(numbers))
```