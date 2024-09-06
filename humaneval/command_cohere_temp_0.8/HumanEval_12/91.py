Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```
This code defines a function `longest` that takes a list of strings as input and returns the longest string. If there's only one string in the list, or if all strings in the list have the same length, it returns the first string using the `or` clause to handle these edge cases. Otherwise, it uses the `max` function with a custom key function to find the longest string in the list based on its length.