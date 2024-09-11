```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None
    
    max_length = 0  # Initialize the maximum length
    longest_string = strings[0]  # Initialize the longest string with the first string in the list
    
    for string in strings:  # Iterate over the list of strings
        if len(string) > max_length:  # Check if the length of the current string is greater than the max length
            max_length = len(string)  # Update the max length
            longest_string = string  # Update the longest string
    
    return longest_string  # Return the longest string


# Test cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```