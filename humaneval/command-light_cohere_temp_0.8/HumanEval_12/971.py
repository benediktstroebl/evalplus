```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: 'c'

strings = ['a', 'bb', 'ccc']
result = longest(strings)
print(result)  # Output: 'ccc'

strings = []
result = longest(strings)
print(result)  # Output: None

strings = ['aa', 'bb', 'ccc']
result = longest(strings)
print(result)  # Output: 'bb'

strings = ['xx', 'yy', 'zz']
result = longest(["xx", "yy", "zz"])
print(result)  # Output: 'zz'
```