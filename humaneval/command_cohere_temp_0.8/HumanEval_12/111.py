```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, strings, as input. It returns either None or the longest string from the input list. The function employs a straightforward algorithm utilizing typing modules to check for empty input and unique string lengths to return the longest string.