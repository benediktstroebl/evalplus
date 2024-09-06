```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    first_str = strings[0]
    if len(strings) == 1:
        return first_str
    max_len = 0
    for str in strings:
        if len(str) > max_len:
            max_len = len(str)
    return str(max_len)

# Unit tests
strings = ["a", "bb", "ccc"]
longest_str = longest(strings)
print("Longest string:", longest_str)
```