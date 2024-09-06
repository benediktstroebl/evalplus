```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    """
    unique(numbers)
    return list(set(numbers))
    """
    return list(set(numbers))
```
The code defines a function remove_duplicates that takes a list of integers as input and returns a new list with all the unique (no duplicate) integers from the input list.