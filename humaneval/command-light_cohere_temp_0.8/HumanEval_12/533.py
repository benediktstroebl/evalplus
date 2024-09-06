```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    first_str = strings[0]
    if len(strings) == 0:
        return None
    for str in strings[1:]:
        if len(str) > len(first_str):
            first_str = str
    return first_str
```