```python
from typing import List
def longest(strings: List[str]):
    """
    Out of list of strings, returns the longest one.
    >>> str.is_list_
    return None
    strings is empty
    >>> longest([])
    >>> longest('')
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
```
The code defines a function called longest that takes a list of strings and returns the longest string in the list. It uses the maximum function with the key argument set to the length of each string, and returns the longest one. The test case at the time shows that the function works correctly.