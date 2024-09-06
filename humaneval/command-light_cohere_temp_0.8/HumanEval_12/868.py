```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string.
    """
    list of strings = strings
    longest_length = len(strings[0])
    for string in strings[1:]:
        if len(string) > longest_length:
            longest_length = len(string)
    return longest_length
```