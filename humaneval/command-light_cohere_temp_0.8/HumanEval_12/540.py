```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return None if strings is empty
    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = []
print(longest(strings))  # Output: None
```
This code defines a function called **longest** that takes a list of strings as an argument. It then checks if the other argument is empty and returns **None**. It then uses the built-in **max** function to get the length of the string and return the longest one.