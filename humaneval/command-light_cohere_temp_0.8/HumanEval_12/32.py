```python
from typing import List
def longest(strings: List[str]):
    """ Out of list of strings, return the longest one
    return the first one in case of multiple strings of the same length.
    if not strings:
        return None
    return strings[0] if len(strings) == 1 else max(strings)
```