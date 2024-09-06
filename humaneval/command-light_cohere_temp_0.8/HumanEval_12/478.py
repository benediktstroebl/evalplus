```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    """
    # List of strings
    strings = list(map(str.strip, strings))
    # Return the longest string
    return max(strings, key=len)
```