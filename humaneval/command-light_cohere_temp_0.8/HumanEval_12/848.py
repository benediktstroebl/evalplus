```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string from a list of strings.
    >>> print(longest(["a", "b", "c", "abc"]))
    ['a']
    >>> print(longest(["aa", "abbb", "ccc", "aa"]))
    'ccc'
    >>> print(longest(["abcde", "abcd", "abcd", "ABCDE"]))
    'ABCDE'
    """
    if not strings:
        return None
    return max(strings, key=len)
```