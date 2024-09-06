```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the longest string in a list of strings"""
    
    if not strings:
        return None
    
    return max(strings, key=len)

# Test cases
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))        # Output: None
print(longest(['')))     # Output: None
print(longest(['a','b']))   # Output: 'a'
```
The function `longest` takes a list of strings as input and returns the longest string. The function also has several test cases to ensure it works as expected.