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
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    
    max_length = 0  # Initialize max length to 0
    longest_str = ""  # Initialize longest string to empty string
    
    for string in strings:  # Iterate over each string in the list
        if len(string) > max_length:  # Check if current string is longer than max length
            max_length = len(string)  # Update max length
            longest_str = string  # Update longest string
    
    return longest_str  # Return the longest string


# Test cases
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```