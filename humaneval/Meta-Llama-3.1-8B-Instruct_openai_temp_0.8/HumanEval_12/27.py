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
    
    # Check if the input list is empty
    if not strings:
        return None
    
    # Initialize the longest string as the first one in the list
    longest_str = strings[0]
    
    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If the current string is longer than the longest one found so far, update the longest one
        if len(string) > len(longest_str):
            longest_str = string
    
    # Return the longest string found
    return longest_str

# Test cases
print(longest([]))  # should print: None
print(longest(['a', 'b', 'c']))  # should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # should print: 'ccc'
```

This script defines the `longest` function which takes a list of strings as input, finds the longest string in the list, and returns it. If the input list is empty, it returns `None`. It includes docstrings and test cases to demonstrate the function's behavior.