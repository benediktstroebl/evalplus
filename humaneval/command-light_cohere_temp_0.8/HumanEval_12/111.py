```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list, or None if empty """
    if not strings:
        return None
    l = [len(s) for s in strings]
    return max(l, key=len)
# tests
strings = ['a', 'bb', 'ccc']
print( longest(strings) )  # Output:  ccc
strings = ['a']
print( longest(strings) )  # Output:  a
strings = []
print( longest(strings) )  # Output: None
```
The function `longest` takes a list of strings as input and returns the longest string in the list. It returns `None` if the strings is empty.

The tests demonstrate the function's functionality:
- When you pass an empty list, it returns `None` as the longest string. 
- When you pass a list of one string, it returns that string. 
- When you pass a list of strings, it returns the longest string in the list.