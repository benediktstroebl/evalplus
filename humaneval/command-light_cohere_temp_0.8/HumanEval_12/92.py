```python
from typing import List
def longest(strings: List[str]):
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of an empty list.
    """
return max(strings, default=None)
"""
# Test
strings = ["a", "b", "c", "aa", "bb", "ccc"]
print(longest(strings)) 
```