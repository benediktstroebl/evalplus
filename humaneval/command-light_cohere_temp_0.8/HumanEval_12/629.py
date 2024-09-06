```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string.

    >>> longest(["a",b"])
    """

    if not strings:
        return None

    max_len = max(len(string) for string in strings)
    return str(max_len)
```