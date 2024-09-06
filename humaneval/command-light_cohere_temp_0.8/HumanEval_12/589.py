Here's a self-contained Python script that defines a function `longest()` that solves the problem you described. It takes a process of selecting the longest string from a list of strings:

```python
from typing import List

def longest(strings: List[str]) ->:
    if not strings:
        return None
    return max(strings, key=len)
```

This function takes a list of strings `strings` as an argument and returns the longest string from the list.