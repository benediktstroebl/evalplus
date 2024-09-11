Here's the self-contained Python script that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string, or None if the input list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```
This script uses the built-in `max` function with the `key` argument set to `len` to find the longest string in the list. If the input list is empty, it returns `None` as specified in the problem.