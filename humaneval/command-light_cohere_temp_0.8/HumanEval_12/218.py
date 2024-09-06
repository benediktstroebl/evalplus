```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple strings of the same length. Return None in case of empty list.
    """
   
    max_length = max(len(x) for x in strings)
    if max_length is None:
        return None
    return strings[0][:max_length]
```