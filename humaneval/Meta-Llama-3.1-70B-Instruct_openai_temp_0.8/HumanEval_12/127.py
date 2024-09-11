```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    >>> longest([]) is None
    True
    >>> longest(['a', 'b', 'c']) == 'a'
    True
    >>> longest(['a', 'bb', 'ccc']) == 'ccc'
    True
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
assert longest([]) is None
assert longest(['a', 'b', 'c']) == 'a'
assert longest(['a', 'bb', 'ccc']) == 'ccc'
```