Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(set(strings).count(longest_string)) == 1 else longest_string[:1]
```

This code defines a function `longest` that takes a list of strings as input and returns either the longest string from the list or the first occurrence of the longest string if there are multiple longest strings. The function handles an empty input list gracefully and returns `None` in such cases. It uses the `max` function with the `key` parameter set to the length of the string to correctly identify the longest string and handles potential ties using the `set` function to count distinct occurrences of each string.