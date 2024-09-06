```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    First, filter the list by length to get the list of the longest strings.
    return the list[max(map(len, strings))].items()
    return max(strings, default='')
```