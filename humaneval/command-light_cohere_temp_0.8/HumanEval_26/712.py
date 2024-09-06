Here's a self-contained Python script with a function `remove_duplicates()` that removes duplicate elements from a list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ 
    From a list of integers, remove all elements that occur more than once.
    Keeps only elements left as is in the input.
    """
    list(set(numbers.items())).
    return list(set(numbers.items()))[1:]
```

The `remove_duplicates` function takes a list of integers as input and removes all duplicate elements. It uses the set() to convert the input list into a set, which automatically removes duplicates. Then, it uses the list() and `set()` again to filter out any elements that are in the set but not in the original list.