```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, returns the length of the longest string.
    """
    longest = lambda s: max(len(x) for x in s)
    return [len(x) for x in strings]
```