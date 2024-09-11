```markdown
### Longest String in a List
#### Problem Statement

Return the longest string from a given list of strings. In case of a tie, return the first string. If the input list is empty, return `None`.

#### Solution

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): A list of strings
    
    Returns:
        Optional[str]: The longest string in the list or None if the list is empty
    """
    # Check if the list is empty
    if not strings:
        return None
    
    # Use the max function with a custom key to find the longest string
    # The key function returns the length of each string
    # In case of a tie, max returns the first string in the list
    return max(strings, key=len)

# Example usage:
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

### Explanation

This solution uses the built-in `max` function with a custom `key` function to find the longest string in the list. The `key` function returns the length of each string, so `max` compares the lengths of the strings to find the longest one. In case of a tie, `max` returns the first string in the list, as desired. If the input list is empty, `max` raises a `ValueError`, so we check for an empty list at the beginning of the function and return `None` in that case.