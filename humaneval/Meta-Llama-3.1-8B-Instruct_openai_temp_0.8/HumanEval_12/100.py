```markdown
### Longest String in List
#### Function to find the longest string in a list

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one.
    Return the first one in case of multiple strings of the same length.
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty
    """
    if not strings:  # check if the list is empty
        return None
    else:
        return max(strings, key=len)  # return the longest string using max() with key=len

# Test cases
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

In this script, we use the built-in `max()` function with the `key` argument set to `len` to find the longest string in the list. If the list is empty, `max()` will raise a `ValueError`, which we avoid by checking if the list is empty before calling `max()`.