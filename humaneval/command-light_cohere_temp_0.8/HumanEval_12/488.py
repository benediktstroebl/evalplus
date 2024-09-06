```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    >>> return ''.join(['a', 'bb', 'ccc'])
    """
    return max(strings, key=len)
```