Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case of an empty list.
    """
    timeit: List[str]
    """
    if not strings:
        return None
    return max(strings)
```