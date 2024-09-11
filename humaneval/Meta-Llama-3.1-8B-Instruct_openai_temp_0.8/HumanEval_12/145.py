### Longest String in a List
#### Python Script

Here's a Python script that implements the `longest` function as described:
```markdown
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
    if not strings:
        return None
    return max(strings, key=len)

# Example usage
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

### Explanation

This script uses the built-in `max` function with the `key=len` argument to find the longest string in the list. If the list is empty, it returns `None` as specified.