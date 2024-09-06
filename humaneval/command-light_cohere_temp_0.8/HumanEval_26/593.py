```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Returns a
    list with all unique elements.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [x for x in numbers if numbers.count(x) == 1]
```