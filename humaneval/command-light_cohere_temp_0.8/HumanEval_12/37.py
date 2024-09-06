```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string from a list of strings.
    Args:
    strings (List[str]): list of strings
    Returns:
    List[str]: longest string
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test case 1: Single string
print(longest(['a'])) # Output: 'a'

# Test case 2: Multiple strings of the same length
print(longest(['a', 'bb', 'ccc'])) # Output: 'ccc'

# Test case 3: Empty list
print(longest([])) # Output: None
```
This Python code defines a function called "longest" that takes a list of strings as input and returns the longest string from that list. The function uses the string length as the key to find the maximum value, and the output is the longest string. This code is also passes all the tests provided in the comments.