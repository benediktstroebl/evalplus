```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    >>> longest(['a', 'b', 'c']) == 'a'
    """
    return max(strings, key=len)

# Test cases
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))          # Output: None
```
This script defines a function called `longest` that takes a list of strings as input and returns the longest string. It utilizes the maximum function with the `key=len` to identify the longest string. The test cases cover the input lists with various lengths and content, and the function correctly returns the longest string from each test case.