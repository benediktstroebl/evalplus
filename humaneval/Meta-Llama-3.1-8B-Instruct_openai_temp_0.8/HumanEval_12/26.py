```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the input list is empty.
    """
    # Check if the input list is empty
    if not strings:
        return None

    # Initialize the longest string with the first string in the list
    longest_string = strings[0]

    # Iterate over the list of strings
    for string in strings:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(string) > len(longest_string):
            longest_string = string

    # Return the longest string
    return longest_string

# Example usage:
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

This script first checks if the input list is empty, in which case it returns None. It then iterates over the list, keeping track of the longest string seen so far. If a longer string is found, it updates the longest string. Finally, it returns the longest string found.