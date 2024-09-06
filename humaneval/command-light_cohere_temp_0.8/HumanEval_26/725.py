```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove elements that occur more than once from the input list.
    Args:
        List[int] - list of integers.
    Returns: list with numbers that occur at most once.
    """
    Returns a list of integers with duplicates removed.
    """

Example:
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
    """
    return [num for num in numbers if num not in set(numbers)]
```