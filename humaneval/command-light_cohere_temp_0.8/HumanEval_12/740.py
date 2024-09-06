```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Find the length of the longest string.
    """
    Take the longest string in a list of strings.
    """
    return max(len(string) for string in strings)
```