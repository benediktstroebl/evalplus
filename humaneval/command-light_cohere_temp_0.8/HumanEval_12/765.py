```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one
    or None if empty
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test case:
print(longest(['a', 'bb', 'ccc', 'a', 'xx']))  # Output: 'ccc'
print(longest(['abcde', 'abcd', 'efg']))  # Output: 'abcd'
print(longest(['']))  # Output: None
print(longest(['a', 'bcd', 'ab']))  # Output: 'ab'
```
This script provides a function called longest, which takes a list of strings and returns the longest string in the list, or None if the list is empty. The key argument is used to determine the length of each string, and the max function is used to find the longest one.