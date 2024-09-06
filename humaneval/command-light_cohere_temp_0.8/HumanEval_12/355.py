```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string from a list of strings """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with some inputs
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['abcde', 'abcba', 'apple']))  # Output: 'abcba'
print(longest([]))  # Output: None
```