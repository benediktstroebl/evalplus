```python
from typing import List
def longest(strings: List[str]): 
    """
    Returns the longest string in the list.
    Parameters:
    strings: list of strings

    Returns:
    string, or None if empty list
    """
    return max(strings, key=len) if strings else None 
# Tests
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = []
strings. strings = ['aa', 'a', 'aaa']
print(longest(strings))  # Output: 'aa'
strings = []
strings = ['a', 'b', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = ['a']
print(longest(strings))  # Output: 'a'
strings = []
strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc')
```
The function `longest` takes a list of strings as input and returns the length of the longest string in the list. It does this using the of the list using the `max` function and the `key` argument set to `len` to get the length of the longest string. The function returns the `None` if the input list is empty.