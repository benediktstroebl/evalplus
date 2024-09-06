```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string in the list.
    >>> longest(['a', 'bc'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    'a'
    >>> longest([])
    None
    >>> longest(['aa', 'aa'])
    'aa'
    >>> longest(['aa', 'a'])
    'aa'
    """
    return max(strings, key=len)
```