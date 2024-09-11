```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): A list of strings.
    
    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string as the first one in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for s in strings:
        # If a string is longer than the current longest string, update the longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string
    return longest_str

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script first checks if the input list is empty. If it is, it returns `None`. Otherwise, it initializes the longest string as the first one in the list and then iterates over the list to find the longest string. If a string is longer than the current longest string, it updates the longest string. Finally, it returns the longest string.