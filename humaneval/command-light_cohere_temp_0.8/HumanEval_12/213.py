```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.

    If input list is empty, return None.

    If list of strings has one or multiple strings of the same length, return the first one.
    """

    list of strings is empty:
    return None
    
    # sort the strings alphabetically
    strings.sort()
    strings in ascending order.
    longest_length = 0
    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > longest_length:
            longest_length = len(string)
            longest_string = string
    return longest_string
```