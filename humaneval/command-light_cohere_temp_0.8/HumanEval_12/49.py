Here's the code:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Find the length of the longest string.
    """
    strings = sorted(strings, key=len, reverse=True)
    return max(strings, default='')
```
The function takes a list of strings and returns the length of the longest string. It sorts the longest string and returns its length, using the max function with a default value of an empty string.