Here's the solution for the problem:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    >>> longest(['a', 'b', 'c']) == 'a'
    >>> longest(['a', 'bb', 'ccc']) == 'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
```
This code defines a function `longest` that takes a list of strings as input and returns the longest string from the list. It does so using the maximum by taking the length of each string and choosing the one with the maximum length.