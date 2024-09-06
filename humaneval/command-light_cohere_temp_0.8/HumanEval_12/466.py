```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from the list.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    """
    if not strings:
        return None
    return max(strings, key=len)
```