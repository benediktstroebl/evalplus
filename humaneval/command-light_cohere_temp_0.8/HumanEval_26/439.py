```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate integers from the input list.
    Input: numbers is a list of integers.
    Duplicate integers are removed.
    Output: Numbers without duplicates
    """
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)
```