Here is a Python script that contains a self-contained function called `longest()` that solves the problem of finding the longest string in a list of strings:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the string is empty.
    >>> longest([])

    Trace the empty list
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
```
This code implements a `longest()` function that takes in a list of strings. It then checks if the input list is empty, and if so, it returns `None`. Otherwise, it finds the longest string using the `max()` function with the `len` function as the key, which gives the length of each string.