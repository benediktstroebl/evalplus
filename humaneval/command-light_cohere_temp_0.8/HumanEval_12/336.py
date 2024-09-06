```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    """
    first = strings[0]
    return_length = len(first)
    for string in strings[1:]:
        if len(string) > return_length:
            return_length = len(string)
    return first if return_length == len(first) else string
```