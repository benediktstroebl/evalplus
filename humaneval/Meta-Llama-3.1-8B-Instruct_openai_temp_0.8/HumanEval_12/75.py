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

    # Use the max function with a key argument to find the longest string
    # The key argument specifies that we want to use the len function to determine the maximum value
    longest_str = max(strings, key=len)

    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings and returns the longest one. If the input list is empty, it returns `None`. The function uses the built-in `max` function with a `key` argument to find the longest string. If there are multiple strings of the same maximum length, it returns the first one in the list. The script includes test cases to verify that the function works correctly.