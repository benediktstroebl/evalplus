Here is a self-contained Python script that implements the longest function, which returns the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    list must not be empty, return None
    """
    if not strings:
        return None
    return max(strings, key=len)
```