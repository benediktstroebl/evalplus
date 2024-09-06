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
This script defines a function `longest` that takes in a list of strings `strings` as input and returns the longest string in the list. If there's only one string in the list, or if all strings in the list have the same length, it returns the first string using the `or` clause in Python. It employs the `max` function with a custom key function based on string length to handle cases where multiple strings of different lengths are present. Additionally, if the input list is empty, it returns `None`.