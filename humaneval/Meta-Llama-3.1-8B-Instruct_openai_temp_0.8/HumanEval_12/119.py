```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): The list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize longest string as the first string

    for string in strings[1:]:  # Iterate over the rest of the strings
        if len(string) > len(longest_str):  # If current string is longer
            longest_str = string  # Update longest string

    return longest_str  # Return the longest string


# Test cases
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'

print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input, and returns the longest string in the list. If the input list is empty, it returns `None`. The function iterates over the list of strings and keeps track of the longest string encountered so far. If there are multiple strings of the same maximum length, it returns the first one it encounters.