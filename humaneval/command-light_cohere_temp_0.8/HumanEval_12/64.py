```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Out of list of strings, returns the longest one.
    >>> longest(['a', 'b', 'c']) --> 'a'
    >>> longest(['a', 'bb', 'ccc']) --> 'ccc'
    >>> longest([]) --> None
    >>> longest(['aa', 'aa', 'aa']) --> 'aa'
    """
    return max(strings, key=len)
```