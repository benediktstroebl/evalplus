```markdown
### Longest String in a List

#### Problem Description

Given a list of strings, return the longest string. If multiple strings have the same maximum length, return the first one encountered. If the input list is empty, return `None`.

#### Solution

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): The list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # If the list is empty, return None.
        return None
    longest_str = strings[0]  # Initialize the longest string with the first one in the list.
    for s in strings[1:]:  # Iterate over the rest of the strings in the list.
        if len(s) > len(longest_str):  # If the current string is longer than the longest string found so far.
            longest_str = s  # Update the longest string.
    return longest_str  # Return the longest string.

# Example usage:
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

#### Explanation

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If multiple strings have the same maximum length, it returns the first one encountered. If the input list is empty, it returns `None`.

The function works by iterating over the list of strings and keeping track of the longest string found so far. If a longer string is encountered, it updates the longest string. Finally, it returns the longest string.

The script also includes example usage of the `longest` function to demonstrate its behavior.