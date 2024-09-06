Here is a self-contained Python function that returns the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    List is not hashable for equality, so we use the == operator instead of the === operator to compare strings.
    return the maximum(strings, key=len)
```

This function takes a list of strings as input and returns the longest string. It does this by using the length of each string in the list and returning the one with the maximum length.