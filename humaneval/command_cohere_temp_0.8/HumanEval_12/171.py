Here's a Python script with a self-contained function that solves the problem:
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
This script includes the `longest` function that takes a list of strings as input and returns either None, or the longest string from the list, following the rules you described. It accounts for cases where there is only one unique string length among the inputs, and also for cases where there are multiple strings of the same length, in which case it returns the first one. It returns None if the input list is empty. 
The `longest` function is self-contained and can be reused as a module in other projects.