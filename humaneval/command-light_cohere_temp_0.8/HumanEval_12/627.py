Here's a Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=len)
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. The `max` function is used to compare the lengths of the strings and return the longest one.