```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate elements from a list of integers, returns a new list with unique values.
    """
    list of integers may have duplicates, but only the first occurrence will be returned.

    Test case:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [i for i in numbers if i not in set(numbers)]
```