```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    Returns the first one in case of length-equals.
    """
   
    return max(strings, key=len) if strings else None
    """
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'

strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = []
print(longest(strings))  # Output: None

strings = ['aa', 'bb', 'cc', 'xx']
print(longest(strings))  # Output: 'xx'
```
The function `longest` accepts a list of strings and returns the length of the longest string. In case the list is empty, it returns `None`.