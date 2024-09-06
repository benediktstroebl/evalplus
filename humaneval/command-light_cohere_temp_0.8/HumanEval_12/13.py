```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string.
    """
    return max(len(x) for x in strings)
```