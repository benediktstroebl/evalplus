```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest([]))  # Should not print anything
print(longest(['a', 'b', 'c']))  # Should print: a
print(longest(['a', 'bb', 'ccc']))  # Should print: ccc
```