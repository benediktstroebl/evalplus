```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns a

    list with all unique integers.
    """
    test:
    Input: [1, 2, 3, 2, 4]
    Output: [1, 3, 4]
    """
    return list(set(numbers))
```