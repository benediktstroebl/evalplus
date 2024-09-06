Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    longest_idx = max(range(len(strings)), key=lambda i: len(strings[i]))
    return strings[longest_idx]
```
This script defines a function called `longest` that takes in a list of strings `List[str]` as an argument and returns either `None` or the longest string in the list. The function first checks if the string is empty, it returns `None`. If there is only one string in the list, it will return that string. If there are multiple strings of the same length, it returns the first one. Finally, it returns the longest string, chaining comparisons to find the maximum string length.