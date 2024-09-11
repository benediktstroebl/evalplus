```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
        strings (List[str]): List of strings
    
    Returns:
        Optional[str]: The longest string, or None if the input list is empty
    """
    # Check if the list is empty and return None if it is
    if not strings:
        return None
    
    # Initialize the longest string to be the first one in the list
    longest_str = strings[0]
    
    # Iterate over the rest of the strings in the list
    for s in strings[1:]:
        # If the current string is longer than the longest one found so far, update the longest one
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string found
    return longest_str

# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines the function `longest` which finds the longest string in a list. It then tests this function with the given test cases. The `if __name__ == "__main__":` block is used to ensure that the test cases are only run when the script is executed directly (not when it's imported as a module).