```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings, or None if empty.
    >>> longest(['a', 'b', 'c'])
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest([])
    """
    return max(strings, default=None)
```