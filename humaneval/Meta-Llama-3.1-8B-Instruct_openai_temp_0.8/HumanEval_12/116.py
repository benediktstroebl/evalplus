Here is the Python script that solves the problem:
```markdown
# Longest String in List
================================

This script returns the longest string in a given list of strings.

### Code
```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # check if the list is empty
        return None
    return max(strings, key=len)  # return the longest string


# Example Usage
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

### Explanation
This script uses the built-in `max` function with a custom `key` function to find the longest string in the list. If the list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one encountered in the list.