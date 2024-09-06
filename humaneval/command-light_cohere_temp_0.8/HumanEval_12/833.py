```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    >>> Return the example list of strings.
    >>> longest(['a'])
    # Will return None
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'a'])
    'aa'
    >>> longest(['aa', 'a', 'a'])
    'aa'
    """
    if not strings:
        return None
    return max(strings, key=len)
```