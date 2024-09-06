```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string.
    """
    Take the string
    """
    max_length = len(strings[0])
    for string in strings[1:]:
        if len(string) > max_length:
            max_length = len(string)
    return max_length
```