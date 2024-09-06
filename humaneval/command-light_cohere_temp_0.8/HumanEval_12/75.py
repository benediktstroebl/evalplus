```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in the list, or None if empty """ 
    if not strings: return None
    return max(strings, key=len)

# Test the function with various lists of strings
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))  # Output: None
print(longest(['aa', 'bb', 'ccc']))  # Output: 'bb'
print(longest([1, 2, 3]))  # Output: '3'
```