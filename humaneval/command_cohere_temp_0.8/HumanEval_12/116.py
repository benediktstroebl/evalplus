Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings.index(max(strings, key=len))
        return strings[max_idx]
```
This script includes the `longest` function that takes a list of strings (`List[str]`) as input and returns either None, or the longest string from the list, following the rules you provided. The script ensures readability and efficiency by using type hints and maximizing the use of built-in Python functionalities.