Here is a self-contained Python script with a function that solves the problem you described:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    >>> return max(strings, key=len)
    """
    return max(strings, key=len)
```

This code defines a Python function called `longest`, which takes a list of strings as input and returns the longest string in that list. It does this by using the `max()` function with the `key=len` argument, which returns the element with the longest index.