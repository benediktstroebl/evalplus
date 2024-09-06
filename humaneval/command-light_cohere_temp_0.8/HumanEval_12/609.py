```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    # Return the string that contains the most number of characters
    """
    return max(strings, key=len)

# Unit tests
strings = ["a", "bb", "ccc", "abc"]
assert longest(strings) == "ccc"

strings = ["a", "bb"]
assert longest(strings) == "bb"

strings = []
assert longest(strings) is None
```