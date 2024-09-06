```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.

    if not strings:
        return None
    l = len(strings)
    max_len = min(len(s) for s in strings) + 1
    max_str = strings[max_len - 1]
    return max_str
```