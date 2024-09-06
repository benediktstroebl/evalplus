```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input
    """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

This approach utilizes Python's list comprehension and the `set()` constructor to efficiently filter out duplicate elements. The function `remove_duplicates()` takes a list of integers as input and returns a list containing only the unique elements, preserving their original order.  It uses a set, `seen`, to keep track of elements encountered previously.