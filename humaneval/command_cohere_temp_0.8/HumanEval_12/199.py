Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings[1:])
```

This code defines a function `longest` that takes a list of strings as input and returns either the longest string from the list or `None` if the list is empty. The function uses the `max` function with a custom key function to find the longest string based on its length. It then checks if the length of the longest string is unique, and if not, it recursively calls `longest` on the remaining strings after skipping the longest string.