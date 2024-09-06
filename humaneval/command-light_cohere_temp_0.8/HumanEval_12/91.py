```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    strings = [str.join("Hello World!") for _ in range(5)]
    return max(strings, key=len)
```