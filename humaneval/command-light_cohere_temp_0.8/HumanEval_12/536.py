```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa'])
    TraceError: List index out of range
    """
    if not strings:
        return None
    return max(strings, key=len)
```