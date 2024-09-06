```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list of strings.
    """
    list of strings is passed as an argument.
    strings = [str for string in strings]
    if not strings:
        return None
    return max(strings, key=len)

# Testing
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = []
print(longest(strings))  # Output: None
```
The problem is to find the longest string in a list of strings. The function longest() takes a input of a list of strings. When the list is empty, it returns None. The function then returns the max function with the key as the length of each string, and the max function with the length of each string will return the longest string.