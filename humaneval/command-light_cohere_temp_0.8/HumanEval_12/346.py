```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from the list.
    """
    strings = [str.join if isinstance(i, str) else i for i in strings]
    return max(strings, key=len)
```

This function uses the `max()` function along with the `key=len` argument to find the element with the maximum length. It takes the result of a single string with the maximum length.