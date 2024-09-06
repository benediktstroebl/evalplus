```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    """
    strings = [string.split() for string in strings]
    return max(strings, key=len)
```
This function splits each string into a list of characters and then uses the `max` function with the `key=len` argument to find the maximum length among all the strings.