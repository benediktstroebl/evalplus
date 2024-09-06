```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    string = "".join(strings)
    return string if string else None
```