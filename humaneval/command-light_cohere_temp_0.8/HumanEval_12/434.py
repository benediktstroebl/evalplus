```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string in a list.
             Returns None if the general case, or all strings are of equal length.
    """
    example:
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['abc', 'abc'])
    'abc'
    >>> longest(['abc', 'abc']) # not equal, returns None
    >>> longest([])
    None
    """
    return None if not strings else strings[0] if len(strings[0]) > len(strings[1]) else strings[1]
```
This function will return the length of the longest string in the list, or None if the list is empty or the strings are all the same length.