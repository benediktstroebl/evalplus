```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case of empty list or input.
    """

    test cases:
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    None
    >>> longest(['a', 'bc', 'abc'])
    'abc'
    """
    return max(strings, key=len)
```