```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    >>> longest(["a",
    'abc' 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=len)
```