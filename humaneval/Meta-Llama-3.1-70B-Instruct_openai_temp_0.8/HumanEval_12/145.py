```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string with the first string in the list
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If the current string is longer than the longest string found so far, update it
        if len(string) > len(longest_str):
            longest_str = string

    # Return the longest string
    return longest_str

# Example usage:
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If there are multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`. The function iterates over the input list to find the longest string and returns it.