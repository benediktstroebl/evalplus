```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    >>> return longest(['a', 'b', 'bc', 'c']) 
    'c'
    >>> longest(['a', 'bb', 'bc', 'cc']) 
    'cc'
    >>> longest(['aa', 'bb', 'ccc'])
    'ccc'
    >>> longest([]) 
    None
    >>> longest(['a', 'bb', 'ccc', 'a'])
    'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```