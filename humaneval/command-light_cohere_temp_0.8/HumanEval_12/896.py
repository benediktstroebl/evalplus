Here is a self-contained Python script that solves the problem of finding the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
```