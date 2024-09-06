```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the length of the longest string.
    """
    return max(len(string) for string in strings)
```