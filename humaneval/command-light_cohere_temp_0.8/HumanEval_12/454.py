```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    >>> longests = ['a', 'bc', 'abc']
    print(longest(longests))  # a
    """
    return max(strings, key=len)
```