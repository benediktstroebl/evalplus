```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string from the list.
    """
    max_length = max([len(s) for s in strings])
    return max(strings, key=len) if max_length is not None else None

#Test cases
strings = ["a", "b", "c"]
longest(strings)
# Output: c

strings = ["a", "bb", "ccc"]
longest(strings)
# Output: c

strings = []
strings. strings longest(strings)
# Output: None
```