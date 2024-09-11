```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): A list of strings.
    
    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    
    longest_str = strings[0]  # Initialize the longest string with the first string in the list
    
    for string in strings[1:]:  # Iterate over the rest of the strings in the list
        if len(string) > len(longest_str):  # Check if the current string is longer than the longest string
            longest_str = string  # Update the longest string if the current string is longer
    
    return longest_str


# Test cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```