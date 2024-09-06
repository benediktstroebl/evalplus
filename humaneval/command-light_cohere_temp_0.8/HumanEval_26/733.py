```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from the input list and return the unique elements.
    """
   
    list of integers with duplicates removed:

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return list(set(numbers))
```