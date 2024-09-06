```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the longest string in the list"""
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ["a", "c", "bb", "ccc"]
print(longest(strings))  # Output: 'ccc'

strings = ["a"]
print(longest(strings))  # Output: 'a')

strings = []
print(longest(strings))  # Output: None
```