```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from the list.
    """
    first: str = strings[0]
    if len(first) > len(strings[1:]):
        return first
    return longest(strings[1:])
```