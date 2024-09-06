Here is a self-contained Python script that solves the problem you have described:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    >> longest(['a', 'b', 'c'])
    'a'
    >> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if not strings:
        return None

    return max(strings, key=len)
```