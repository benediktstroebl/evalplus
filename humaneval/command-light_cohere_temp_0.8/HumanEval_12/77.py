```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'bb', 'ccc'])
    ccc
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with a list of strings
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'bb'
print(longest(['a', 'b']))  # Output: 'a'
```