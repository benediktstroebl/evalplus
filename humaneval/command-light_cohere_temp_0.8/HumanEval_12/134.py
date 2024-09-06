```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list of strings.
    """
    strings = [x for x in strings if x] 
    return max(strings, key=len) if strings else None
```