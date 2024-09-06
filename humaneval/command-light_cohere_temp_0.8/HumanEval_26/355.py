```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once from a list of integers.
    """
    List[set](numbers)
    return List(set(numbers))
```

This function uses the `set` function from the Python standard library to remove duplicate values from the input list and then convert the set back to a list. 
This ensures a unique list of integers.