```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['a'])
    'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```