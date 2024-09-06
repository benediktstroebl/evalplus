```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns a unique elements in order of their occurrence.
    """
    list comprehension to create a set of unique elements.
    return [list of integers that appear only once in the original list
    """
    set_of_unique = set(numbers)
    return [x for x in set_of_unique if x not in numbers]
```