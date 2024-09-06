```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    >>> longest([]) --> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([x for x in ['aa', 'bb', 'ccc']])
    'ccc'
    >>> longest(['a', 'bb', 'ccc'])[:-3]
    'ccc'
    """
    return max(strings, key=len)
```