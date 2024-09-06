Here is a self-contained Python script that includes a function that correctly determines the longest string in a list of strings:
```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one or None if empty """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with various inputs
test_strings = ['a', 'b', 'c', 'bb', 'ccc']
print(longest(test_strings))  # Output: 'ccc'
test_empty = []
print(longest(test_empty))  # Output: None
test_single = 'a'
print(longest(test_single))  # Output: 'a'
```
This script defines a function called longest that takes a list of strings and returns the longest string. The function first checks if the strings list is empty, and if so, returns None. Otherwise, it uses the max function with the length of the string as the key to find the maximum length and returns the longest string.