```markdown
### Longest String Finder

A Python function to find the longest string in a list of strings. If multiple strings have the same maximum length, it returns the first one encountered. If the input list is empty, it returns `None`.

#### Code

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

# Test cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```

#### Notes

*   We use the built-in `max()` function with the `key` argument set to `len` to find the longest string in the list.
*   If the input list `strings` is empty, we immediately return `None`.
*   For test cases, we cover the scenarios where the input list is empty and where there are multiple strings with the same maximum length.