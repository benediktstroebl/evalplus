```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'b', 'a'])
    ['a', 'b', 'a']
    >>> return longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> return longest([])
    None
    >>> return longest(['a', 'aa', 'aaaa'])
    'aaaa'
    """
    if not strings:
        return None
    return max(strings, key=len)
```  This code defines a function called `longest` that takes a list of strings and returns the longest string from that list. It also provides some test cases that demonstrate how the function works.