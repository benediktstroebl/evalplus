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
        Optional[str]: The longest string or None if the input list is empty.
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string with the first string in the list
    longest_string = strings[0]
    
    # Iterate over the list of strings
    for string in strings:
        # If the current string is longer than the longest string, update the longest string
        if len(string) > len(longest_string):
            longest_string = string
    
    # Return the longest string
    return longest_string

# Test the function
print(longest([]))  # Should return None

print(longest(['a', 'b', 'c']))  # Should return 'a'

print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. In case of multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`. The script also includes test cases to demonstrate its correctness.