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
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize the longest string as the first one
    max_len = len(longest_str)  # Initialize the max length as the length of the first string

    for s in strings:  # Iterate over the rest of the strings
        if len(s) > max_len:  # If the current string is longer than the max length
            longest_str = s  # Update the longest string
            max_len = len(s)  # Update the max length

    return longest_str

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```