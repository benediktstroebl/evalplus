```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the length of the longest string.
    >>> longest(['a', 'b', 'c'])
    >>> 'a'
    """
    return max(strings, key=len)
```