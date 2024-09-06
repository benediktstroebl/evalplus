```python
from typing import List
def longest(strings: List[str]):
    """
    Out of list of strings, return the longest one.
    >>> str.isinstance an longest([])
    string
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['aa', 'a'])
    'aa'
    >>> longest(['aa', 'aa', 'a'])
    'aa'
    """
    return max(strings, key=len)
```