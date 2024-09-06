Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings[1:])
```

This script defines a function `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function follows the specified behavior using the `typing` module to ensure type safety.