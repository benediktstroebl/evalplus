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
    
    # Check if the input list is empty
    if not strings:
        return None
    
    # Initialize the longest string with the first string in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for string in strings:
        # Check if the current string is longer than the longest string
        if len(string) > len(longest_str):
            # Update the longest string
            longest_str = string
    
    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. The function iterates over the list of strings and keeps track of the longest string found so far. The test cases at the end verify that the function works as expected.