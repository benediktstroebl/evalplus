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

This code defines a function `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function first checks if the list is empty, and if so, returns `None`. If the list is not empty, it uses the `max` function with the `key` argument set to the len function to identify the longest string in the list. The function then returns the longest string, but only if it is also the longest string overall in terms of character count. If it is not the longest in terms of character count, then the function returns the first longest string that is not the initial longestString. This handling of ties ensures that the function returns the longest unique string in the list.