```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    first_length = 0
    longest_str = ""
    for string in strings:
        if len(string) > first_length:
            first_length = len(string)
            longest_str = string
    return longest_str
```