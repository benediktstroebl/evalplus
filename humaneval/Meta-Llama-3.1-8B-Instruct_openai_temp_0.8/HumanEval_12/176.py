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
        Optional[str]: The longest string in the input list or None if the list is empty.
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string as the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings
    for string in strings:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(string) > len(longest_str):
            longest_str = string

    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses a simple iterative approach to find the longest string in the input list. If the input list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one encountered.