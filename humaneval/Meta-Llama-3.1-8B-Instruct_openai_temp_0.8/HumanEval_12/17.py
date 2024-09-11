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

    # Check if the list is empty
    if not strings:
        # If the list is empty, return None
        return None

    # Initialize the longest string as the first string in the list
    longest_str = strings[0]

    # Iterate over the list of strings
    for string in strings:
        # Check if the current string is longer than the longest string found so far
        if len(string) > len(longest_str):
            # If it is, update the longest string
            longest_str = string

    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines the `longest` function, which takes a list of strings as input and returns the longest string in the list. The function first checks if the list is empty, in which case it returns `None`. If the list is not empty, it iterates over the list and keeps track of the longest string found so far. Finally, it returns the longest string. The script also includes test cases to verify that the function works correctly.