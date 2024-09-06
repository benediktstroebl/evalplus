```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from the list of strings.
    """
    return max(strings) if strings else None
```