```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    >>> return longest(['a', 'bb', 'ccc'])
    >>> 'ccc'
    """
    if not strings:
        return None
    return max(len(x) for x in strings)
```