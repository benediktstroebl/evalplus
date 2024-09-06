```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list"""
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 3
strings = ["ab","ac","ba"]
print(longest(strings))  # Output: 2
strings = []
strings. strings string = "hello"
strings. string longest()  # Output: 6
```