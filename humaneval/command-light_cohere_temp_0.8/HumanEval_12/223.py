```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in the list
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['ab', 'ccc', 'aaaa']))  # Output: 'ccc'
print(longest(['a', 'b', 'aa', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))  # Output: None
print(longest(['aa', 'aa']))  # Output: 'aa'
```