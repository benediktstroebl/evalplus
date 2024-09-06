```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string.
    """
    longest = str(max(len(s), default=''))
    return longest
```