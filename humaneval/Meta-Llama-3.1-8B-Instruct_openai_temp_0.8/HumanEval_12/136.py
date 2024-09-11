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
    # Check if the list is empty and return None if it is
    if not strings:
        return None

    # Return the first string in the list as the longest one
    # This will be overwritten if a longer string is found
    longest_string = strings[0]

    # Iterate over the rest of the list
    for string in strings[1:]:
        # If the current string is longer than the longest string found so far
        if len(string) > len(longest_string):
            # Update the longest string
            longest_string = string

    # Return the longest string found
    return longest_string

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, the function returns `None`. If there are multiple strings of the same length, the function returns the first one it encounters. The script also includes test cases to demonstrate the function's behavior.