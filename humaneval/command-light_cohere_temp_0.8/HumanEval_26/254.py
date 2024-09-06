```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes duplicates from the input list.
    Args: 
        - A list of integers. 
    Returns: 
        A list of integers without duplicates.
    """
    Test: 
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    >>> remove_duplicates([1, 2, 2, 3])
    [1, 2, 3]
    """
    return [x for x in numbers if not in numbers[:1]]
```