```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    Returns the first one in case of length-equality. Returns None if empty input list.
    """
   icular"""
    verifications:
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    None
    >>> longest(['a', 'b'])
    'a'
    >>> longest(['aa'])
    None
    >>> longest([])
    None
    >>> longest(['aa', 'bb', 'ccc'])
    'bb'
    """
    return max(strings, key=len) if strings else None
```
This code is a Python script with a self-contained function `longest` that solves the problem of finding the longest string in a list. The function uses the max function to find the maximum value of each string's length, and returns the longest string. The `key=len` argument is used to ensure that the maximum is taken from the list's strings, not just the first one.