```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
```