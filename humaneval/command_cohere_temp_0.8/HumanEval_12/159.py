```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longestString = max(strings, key=len)
    return longestString if len(longestString) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longestString]
    )
```