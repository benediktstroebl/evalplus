```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    longest_length = max(len(str) for str in strings)
    return strings[strings.index(longest_length)]
```
Do you require any further assistance with coding or debugging related to this problem?