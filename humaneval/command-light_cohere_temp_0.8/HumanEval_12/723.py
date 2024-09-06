```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    >>> longest(['a', 'b', 'c']) == 'a'
    """
    return max(strings, key=len)
```