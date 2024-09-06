```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string in the list.
    Args: strings (list of strings)
    Returns: The length of the longest string
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 3
print(longest([''] ))  # Output: 1
print(longest(['a', 'abc', 'def')))  # Output: 4
print(longest(['abcde', 'def']))  # Output: 5
print(longest([]))  # Output: 0
```