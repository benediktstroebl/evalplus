```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string from the list.
    """
    string = "".join  # just to avoid the default argument case
    return strings.get(0, 0) if len(strings) == 0 else max(strings, key=len)
```