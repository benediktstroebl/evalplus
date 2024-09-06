```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases for longest function
strings = ['a', 'b', 'c']
strings. longest = ['a', 'bb', 'ccc']
strings = ['a', 'bc', '']
strings = ['abcde', 'abcf']
strings = ['', 'a', 'bc']
strings = ['a', 'bb', '']

# Verify results
assert longest(strings) == 'a'
assert longest(strings.find) == 'bb'
```