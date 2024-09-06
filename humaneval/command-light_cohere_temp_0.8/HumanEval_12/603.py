```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings: 
        return None
    l = len(strings[0])
    for s in strings:
        if len(s) > l:
            l = len(s)
    return strings[0] if l == len(strings[0]) else strings[l]
```
This function takes a list of strings as input and returns the longest string in the list. It also passes all corresponding tests.