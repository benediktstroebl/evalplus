Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longestStr = max(strings, key=len)
    return longestStr if len(longestStr) == max(map(len, strings)) else longest(list(filter(lambda x: x == longestStr, strings)))
```

The function uses the `max` function with a custom `key` argument to find the longest string in the list and handles the cases of multiple longest strings and an empty list correctly.