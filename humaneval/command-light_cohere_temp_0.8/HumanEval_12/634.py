```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in a list """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
print(longest(['a', 'b', 'c', 'a']))  # Output: 'a'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))        # Output: None
```