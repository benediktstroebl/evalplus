```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    ['a']
    >>> longest(['aa', 'a', 'aaa'])
    ['aaa']
    >>> longest([])
    None
    >>> longest(['aa', 'bb', 'a'])
    ['aa']
    """
    return max(strings, key=len)
```