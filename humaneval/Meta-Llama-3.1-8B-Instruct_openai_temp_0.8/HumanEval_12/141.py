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
    Optional[str]: The longest string or None if the input list is empty.

    Examples:
    >>> longest([])
    None

    >>> longest(['a', 'b', 'c'])
    'a'

    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string with the first string in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for s in strings:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string
    return longest_str

# Test the function
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # a
print(longest(['a', 'bb', 'ccc']))  # ccc
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one. The script includes docstrings to explain the purpose and behavior of the function, and it includes test cases to demonstrate its correctness.