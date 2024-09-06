```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the longest string in the list."""
    if not strings:
        return None
    # Sort the list of strings
    strings.sort()
    longest to maintain the first item of the list
    return strings[0]
```