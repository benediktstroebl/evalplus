Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    longest_string = max(strings, key=len)
    return longest_string
```

This script defines a function called `longest` that takes in a list of strings as input and returns either None, or the longest string in the list. If the input list contains only one unique string, the function returns the first occurrence of that string. The `longest` function uses the `max` function with a custom key to find the longest string. The `key` argument is a function that tells the `max` function how to determine the best string, in this case, it is the length of the string.