Here's a Python script with a self-contained function that solves the problem:
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

This code defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list or None if the list is empty. The function first checks if the list is empty, and if so, returns None. If the list is not empty, it uses the `max` function with the `key` parameter set to the len function to identify the longest string in the list. The function then returns the longest string, but only if it is uniquely the longest string amongst all strings in the list; otherwise, it recursively calls itself, excluding the longest string, to find the true longest string in the list.