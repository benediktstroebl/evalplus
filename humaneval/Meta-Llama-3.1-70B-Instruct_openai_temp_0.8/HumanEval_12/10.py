```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from a list of strings. If there are multiple strings of the same length,
    it returns the first one. If the input list is empty, it returns None.
    
    Args:
    strings (List[str]): A list of strings.
    
    Returns:
    Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:
        return None
    
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses Python's built-in `max` function with the `key` argument to find the longest string in the list. The `key` function `len` returns the length of each string, allowing `max` to compare them by length. If the input list is empty, it returns `None` as per the problem statement.