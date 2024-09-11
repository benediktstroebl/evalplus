```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    # Check if input list is empty
    if not strings:
        return None
    
    # Initialize longest string with the first string in the list
    longest_str = strings[0]
    
    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If a longer string is found, update longest_str
        if len(string) > len(longest_str):
            longest_str = string
    
    return longest_str

# Test cases
print(longest([]))  # Should not print anything (None)
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```