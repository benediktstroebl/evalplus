```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    Args:
        strings (List[str]): List of strings to compare length 
    Returns:
        Optional[str]: Returns the longest string, or None if empty input list
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with various inputs
strings = ['a', 'b', 'c', 'a']
print(longest(strings))  # Output: 'a'
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = []
print(longest(strings))  # Output: None
```
The code defines a Python function called longest that takes a list of strings as input and returns the longest string in the list, or None if the input list is empty. The function uses the test with various inputs and passes the tests successfully.