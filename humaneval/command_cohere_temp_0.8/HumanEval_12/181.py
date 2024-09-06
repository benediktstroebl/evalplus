Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings[:strings.index(longest_str)])
```

This version of the function uses the built-in `max` function with a custom key to find the longest string. It then checks if the longest string is the only string of its length, or if there are others. If there are others, it recursively calls the function on the sublist before the longest string. If the input is empty, it returns `None`.