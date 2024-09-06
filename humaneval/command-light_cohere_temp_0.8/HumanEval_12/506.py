```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Out of list of strings, returns the longest one."""
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ["a", "b", "c"]
print(longest(strings))  # Output: 'c'
strings = ["aa", "bb", "ccc"]
print(longest(strings))  # Output: 'ccc'
strings = []
strings. bl_5'
# Output: None
strings = ["a", "bb", "ccc"]
strings.a = "best"
print(longest(strings))  # Output: 'best'
``` 
This script defines a Python function called "longest," which accepts a list of strings and returns the longest string in that list. The function employs the max function with a key parameter set to len, which compares the lengths of the strings in the list. This method ensures the maximum length is obtained.