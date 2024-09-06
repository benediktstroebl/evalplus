Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
This script includes the `longest` function that takes a list of strings `strings` as input and returns the longest string from the list. If the list contains multiple strings of the same length, it returns the first one. If the list is empty, it returns `None`. The script ensures correctness and handles edge cases appropriately.