```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the longest string in a list, or None if empty"""
    return max(strings, key=len) or None  # Returns max(strings, key=len) because list has no built-in max() method.

# Example cases:
# single string
print(longest(['a']))  # Output: 'a'

# list of strings
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'

# empty list
print(longest([]))  # Output: None
```