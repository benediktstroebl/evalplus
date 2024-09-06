```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    > Returns the longest string from a list of strings.
    """
    return strings and [...max(strings)] if strings else None
    """
    # return the max string from the list
    return max(strings, key=len)
```