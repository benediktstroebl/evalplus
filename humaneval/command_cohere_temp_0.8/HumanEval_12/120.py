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

This code defines a function `longest` that takes a list of strings as input and returns either the longest string in the list, the first string if multiple strings have the same maximum length, or `None` if the input list is empty. The logic revolves around leveraging the `max` function with a custom key function that specifies the sorting criteria using string length.

For an empty list, `None` is returned. If only one string is present, it is directly returned. When there's a list of strings with different lengths, the longest ones are extracted using the `max` function, considering only the length of each string as the sorting metric.