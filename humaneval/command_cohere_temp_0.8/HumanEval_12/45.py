```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longestString = max(strings, key=len)
    return longestString if len(longestString) == max(map(len, strings)) else longest(
        [s for s in strings if s != longestString]
    )
```

This code uses the `max` function with `key=len` to identify the longest string and then recovers in the case of a tie by recursively calling the function on the rest of the list. As the base case, if the list is empty, it returns `None`.