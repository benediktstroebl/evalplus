```markdown
### Longest String Finder
#### Python Script
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
        Optional[str]: The longest string, or None if the input list is empty.

    Examples:
        >>> longest([])
        None

        >>> longest(['a', 'b', 'c'])
        'a'

        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script uses the built-in `max` function with the `key` argument set to `len` to find the longest string in the list. If the list is empty, it returns `None`. The `key` argument specifies that we want to compare the strings based on their length, not their lexicographical order.