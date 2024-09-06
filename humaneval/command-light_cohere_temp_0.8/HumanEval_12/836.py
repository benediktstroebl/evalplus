```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string.
    >>> longest(['a', 'b', 'c']) --> 'a'
    >>> longest(['a', 'bb', 'ccc']) --> 'ccc'
    >>> longest([]) --> None
    >>> longest(['a', 'bb', 'ccc', 'xx'])
    ['ccc']
    """
    if not strings:
        return None
    return max(strings, key=len)
```