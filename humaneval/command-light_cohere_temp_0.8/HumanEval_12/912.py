```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the length of the longest string.
    >>> longest(['a', 'b', 'c']) == 3
    >>> longest(['abc', 'a']) == 3
    """
    if not strings:
        return None
    return max(len(string) for string in strings)
```