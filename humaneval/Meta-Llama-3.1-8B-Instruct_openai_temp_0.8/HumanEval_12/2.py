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
        Optional[str]: The longest string in the list or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None
    
    longest_str = strings[0]  # Initialize the longest string as the first one in the list
    max_length = len(longest_str)  # Store the length of the longest string

    for string in strings:  # Iterate over the list of strings
        if len(string) > max_length:  # Check if the length of the current string is greater than the max length
            longest_str = string  # Update the longest string
            max_length = len(string)  # Update the max length

    return longest_str  # Return the longest string

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input, and returns the longest string in the list. If the list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one encountered. The test cases at the end demonstrate the function's behavior.