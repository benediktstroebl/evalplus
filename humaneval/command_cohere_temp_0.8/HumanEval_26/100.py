```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order as input. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This code defines a function `remove_duplicates` that takes a list of integers as input and returns a list of unique integers from the input list. It uses a set `seen` to keep track of seen elements and appends elements not in the set to the `result` list.