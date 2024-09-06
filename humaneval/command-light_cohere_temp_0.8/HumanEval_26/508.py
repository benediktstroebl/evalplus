```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicates from a list of integers.
    >>> numbers = [1, 2, 3, 2, 4]
    return remove_duplicates(numbers)
    [1, 3, 4]
    """
    return [x for x in set(numbers) if numbers.count(x) == 1]
``` 
The `remove_duplicates` function takes a list of integers and returns a new list with all unique integers. The function uses the set and the `count()` method to remove any duplicate elements from the input list.