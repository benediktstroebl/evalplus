```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'b', 'ccc'])
    'ccc'
    >>> longest(['a', 'bb', 'bc'])
    'bb'
    >>> longest(['abc', 'b', 'ab'])
    'abc'
    >>> longest([])
    None
    """
    if not strings:
        return None
    
    max_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return strings[max_length]
```