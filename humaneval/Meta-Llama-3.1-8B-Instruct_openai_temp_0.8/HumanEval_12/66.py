```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Parameters:
    strings (List[str]): A list of strings
    
    Returns:
    Optional[str]: The longest string from the list or None if the list is empty
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

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```