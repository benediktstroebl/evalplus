```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one
    """
    return max(strings, key=len) if strings else None

# Unit tests
strings = ['a', 'b', 'c', 'd']
longest_result = longest(strings)
assert longest_result is not None, "Input list is empty, unable to determine longest string"
assert len(longest_result) == 4, "The returned longest string does not match the length of the input list"
print(longest_result)  # Output: c
```