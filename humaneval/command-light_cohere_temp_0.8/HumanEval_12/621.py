```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list of strings.
    """
    list of strings = list(map(str.strip, strings))
    if len(strings) == 0:
        return None
    return max(strings)
```