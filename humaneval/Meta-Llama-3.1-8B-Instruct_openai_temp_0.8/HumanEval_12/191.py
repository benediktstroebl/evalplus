```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
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
    
    # Iterate over the rest of the strings in the list
    for s in strings[1:]:
        # If a string is longer than the current longest string, update the longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one it encounters. The test cases at the end demonstrate the function's behavior.