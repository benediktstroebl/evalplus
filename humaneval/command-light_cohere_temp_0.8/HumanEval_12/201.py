Here's the code:
```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string.
    >>> longest(['a', 'b', 'ccc'])
    6
    """
    max_length = len(strings[0])
    for string in strings[1:]:
        if len(string) > max_length:
            max_length = len(string)
    return max_length
```

This script defines a function `longest` that takes a list of strings as input and returns the length of the longest string. It uses the approach to find the longest string, comparing the length of each string in the list against the current maximum length.