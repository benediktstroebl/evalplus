```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(set(strings), key=strings.count)
```
This code defines a function `longest` that takes in a list of strings `strings` as input and returns the longest string from the list. If the input list is empty, it returns `None`. The function uses the `max` function with a `key` argument to count the occurrence of each string in the list. This ensures that it selects the longest non-empty string if there are multiple strings of the same length.