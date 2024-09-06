```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    """
    list contains at least one string
    """
    if not strings:
        return None

    return max(strings, key=len)
```