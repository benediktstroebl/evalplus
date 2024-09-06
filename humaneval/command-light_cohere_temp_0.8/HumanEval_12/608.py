```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one
    Return the first one in case of multiple strings of the same length.
    >>> longest(['a', 'b', 'b'])
    ['a']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    ''
    >>> longest(['aa', 'bb', 'ccc'])
    'bb'
    >>> longest(['aa', 'aa'])
    'aa'
    """
    return strings[0] if len(strings) > 0 else None
```