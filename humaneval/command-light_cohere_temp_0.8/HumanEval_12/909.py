```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    > Returns the longest string in the list.
    """
    list of strings = list(strings)
    if len(strings) == 0:
        return None
    # Sort the list to ensure uniqueness, then return the first element
    return strings[0]
```