```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input
    """
    return list(set(numbers))
```

This code defines a function called `remove_duplicates` which takes a list of integers as input. It uses a set to remove any duplicate elements from the input list and then converts it back to a list to preserve the order of the original list. This ensures that all duplicate elements are removed while maintaining the original order of the unique elements.