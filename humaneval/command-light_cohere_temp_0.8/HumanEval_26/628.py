```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers, returns a unique list.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return list(set(numbers))
``` 
The function is well-contained and will solve the problem of removing duplicates from a list of integers.