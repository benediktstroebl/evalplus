```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    strings = ['a', 'bb', 'ccc']
    return max(strings, key=len)
    """
# Test cases
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = ['a'] * 3  # Output: 'a'

strings = []  # Output: None

strings = ['a', 'bb', 'ccc']
strings. Active list with only one string.  # Output: None
```
This script defines a function called `longest` that takes a list of strings as input and returns the longest string from that list. The function uses the max function with the `key=len` argument to return the longest string.