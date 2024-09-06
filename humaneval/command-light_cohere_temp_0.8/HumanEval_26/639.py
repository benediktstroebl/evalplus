```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from a list of integers and return the unique list.
    """
    Input list of integers.
    Returns a unique list of integers
    """
    set(numbers) = list(set(numbers))
    return [i for i in set(numbers) if i not in numbers]
```
This Python function called `remove_duplicates` takes a list of integers as input and returns a new list with duplicate elements removed. The function first converts the unique elements using `set()` and then filters out any duplicate elements using a list comprehension.