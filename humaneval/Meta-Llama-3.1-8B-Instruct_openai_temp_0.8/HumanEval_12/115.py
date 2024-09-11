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
    # Check if the list is empty, return None in this case
    if not strings:
        return None
    
    # Use the max function with a key argument to find the longest string
    # The key argument specifies that we want to use the len function to determine the maximum string
    longest_string = max(strings, key=len)
    
    return longest_string

# Test cases
if __name__ == "__main__":
    print(longest([]))  # Should print: None
    print(longest(['a', 'b', 'c']))  # Should print: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses the `max` function with a `key` argument to find the longest string in the list. The `key` argument specifies that we want to use the `len` function to determine the maximum string. If the input list is empty, the script returns `None`. The test cases at the end of the script verify that the function works correctly.