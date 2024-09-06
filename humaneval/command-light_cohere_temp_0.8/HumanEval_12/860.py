Here is a self-contained Python script that defines a function `longest` that solves the problem of returning the longest string from a list of strings:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:  # empty list
        return None
    l = len(strings)

    for i in range(len(strings)):
        if len(strings[i]) > l:
            l = len(strings[i])

    return strings[l - 1]
```

This code snippet has a working function `longest` that takes a list of strings and returns the longest string. It handles the process of checking for an empty list and comparing string lengths before returning the longest one.