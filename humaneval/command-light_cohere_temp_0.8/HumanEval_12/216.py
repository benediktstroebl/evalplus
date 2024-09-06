```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    >>> longest(['a', 'b', 'c']) --> 'a'
    >>> longest(['aa', 'bb', 'ccc']) --> 'ccc'
    >>> longest([]) --> None
    """
    # your code here
    if not strings:
        return None
    return max(strings, key=len)
```