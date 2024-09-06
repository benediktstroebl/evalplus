Here is a self-contained Python script with a function that solves the problem of returning the longest string among a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    > Returns the longest string in the list among all strings. 
    """
    Takes a string list as input and returns the longest string.
    return the string found in list with the maximum length.
    if not strings:
        return None
    return max(strings, key=len)
```