```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in a list.
    >>> longest(['a', 'b', 'c']) == 'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```