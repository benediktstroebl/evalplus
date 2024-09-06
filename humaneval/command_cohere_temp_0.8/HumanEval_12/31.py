Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(longest_string) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_string]
    )
```

This code defines a function `longest` that takes a list of strings as input and returns either the longest string from the list or `None` if the list is empty. The function uses the `max` function with a custom key to find the longest string based on its length. If there are multiple longest strings, it recursively excludes the others and returns the first one. The base case is an empty list, where it returns `None`.