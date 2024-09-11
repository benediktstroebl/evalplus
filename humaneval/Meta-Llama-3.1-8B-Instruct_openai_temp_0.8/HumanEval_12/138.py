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
    # Check if the list is empty
    if not strings:
        return None

    # Initialize the longest string as the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings
    for string in strings:
        # If the current string is longer than the longest string found so far
        if len(string) > len(longest_str):
            # Update the longest string
            longest_str = string

    # Return the longest string
    return longest_str

# Example usage:
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

This script defines a function `longest` that takes a list of strings and returns the longest string. If the list is empty, it returns `None`. If there are multiple strings of the same length, it returns the first one. The function uses a simple iterative approach to find the longest string.