```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from a list of integers.
    Unique elements are kept as-
     return a new list with all distinct elements.
    """
    list(set(numbers))
    """
    return list(set(numbers))
```