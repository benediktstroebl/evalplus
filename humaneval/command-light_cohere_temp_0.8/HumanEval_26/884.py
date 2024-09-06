```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from a list of integers.
    Return a list of unique integers.
    """
"""
    seen = set()
    result = [x for x in numbers if x not in seen]
    return result
```