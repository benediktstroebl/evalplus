```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

This script defines a function named `remove_duplicates` which takes a list of integers as input and returns a new list that does not contain any duplicate integers. It uses a set called `seen` to keep track of integers that have already been encountered. It then uses a list comprehension to filter out any integers that have already appeared in the input list.