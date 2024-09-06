Here is a self-contained Python script that includes a function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    >>> longest([]) --> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'ab', 'aba'])
    'aba'
    >>> longest(['aa', 'bb', 'BBC'])
    'bb'
    """
    if not strings:
        return None
    return max(strings, key=len)
```