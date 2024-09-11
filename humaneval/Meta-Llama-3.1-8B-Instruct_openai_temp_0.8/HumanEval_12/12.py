### Longest String from List
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): A list of strings
    
    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the longest string as the first one in the list
    longest_str = strings[0]
    
    # Iterate over the list to find the longest string
    for string in strings:
        # If a string is longer than the current longest string, update the longest string
        if len(string) > len(longest_str):
            longest_str = string
    
    # Return the longest string
    return longest_str

# Example usage:
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the input list is empty, it returns `None`. The function iterates over the list to find the longest string, and in case of a tie, it returns the first string of the longest length. The example usage at the end demonstrates how to use the function.