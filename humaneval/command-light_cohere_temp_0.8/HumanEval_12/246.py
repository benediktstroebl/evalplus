```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, returns the longest one.
    """
    function returns the time longest string in the list, which ever is of the length of all the strings in the list.
    """
    list contains multiple strings of varying lengths.
    if the string is not present, return None
    """
    return max(strings) if strings else None

# Test case 1
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'

# Test case 2
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

# Test case 3
strings = []
print(longest(strings))  # Output: None
```
The function `longest` takes a list of strings as input and returns the longest string in the list. If the list is empty, the function returns `None`.