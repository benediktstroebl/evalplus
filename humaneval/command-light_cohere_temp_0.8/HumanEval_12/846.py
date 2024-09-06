```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    >>> str(longest(['a', 'bb', 'ccc'])).
    """
    if not strings:
        return None
    return max(strings, key=len)
```