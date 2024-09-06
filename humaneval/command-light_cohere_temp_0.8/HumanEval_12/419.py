```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """
    Find the longest string in a list of strings.
    Return the string if one, or list is empty.
    >>> longest([])
    Trace this function returns None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
```