```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    
    # Check if the list is empty
    if not strings:
        return None  # Return None for empty list
    
    # Initialize longest_str with the first string in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for string in strings:
        # If the current string is longer than longest_str, update longest_str
        if len(string) > len(longest_str):
            longest_str = string
    
    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. In case of multiple strings of the same length, it returns the first one. The test cases at the end verify the function's behavior.