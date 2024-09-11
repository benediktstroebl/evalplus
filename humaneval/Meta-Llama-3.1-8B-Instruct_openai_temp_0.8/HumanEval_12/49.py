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
    Optional[str]: The longest string or None if the list is empty
    """
    # Check if the list is empty and return None if it is
    if not strings:
        return None
    
    # Use the built-in max function with a key of len to find the longest string
    # The key parameter of the max function tells it to use the length of each string when comparing
    longest_string = max(strings, key=len)
    
    # Return the longest string
    return longest_string


# Test cases
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'

print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script does the following:

*   It defines a function `longest` that takes a list of strings as input.
*   It checks if the list is empty, and if it is, it returns `None`.
*   It uses the built-in `max` function to find the longest string in the list. The `key` parameter of `max` is set to `len` so that `max` compares the lengths of the strings when deciding which one is the longest.
*   It prints the results of several test cases to demonstrate how the `longest` function works.