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
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    # Check if the list is empty and return None if it is
    if not strings:
        return None
    
    # Initialize the longest string as the first string in the list
    longest_str = strings[0]
    
    # Iterate over the list of strings
    for s in strings:
        # If the current string is longer than the longest string found so far, update the longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string
    return longest_str

# Test the function
if __name__ == "__main__":
    print(longest([]))  # Expected output: None
    print(longest(['a', 'b', 'c']))  # Expected output: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. If there are multiple strings of the same length, it returns the first one in the list. The script also includes test cases to verify the function's behavior.