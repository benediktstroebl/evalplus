```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list"""
    if not strings:
        return None
    return max(strings, key=len)
```