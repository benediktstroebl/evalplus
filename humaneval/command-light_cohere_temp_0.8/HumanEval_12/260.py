Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string in the list.
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)
```