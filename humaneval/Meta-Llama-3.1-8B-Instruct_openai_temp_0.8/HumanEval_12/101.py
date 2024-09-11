```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:  # If the list is empty, return None
        return None
    
    longest_str = strings[0]  # Initialize the longest string as the first one
    for s in strings:  # Iterate over the rest of the list
        if len(s) > len(longest_str):  # If we find a longer string
            longest_str = s  # Update the longest string
    
    return longest_str  # Return the longest string


# Test cases
if __name__ == "__main__":
    # Empty list
    assert longest([]) is None
    
    # Single element list
    assert longest(['a']) == 'a'
    
    # Multiple element list
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    
    # All strings are the same length
    assert longest(['a', 'b', 'c']) == 'a'
```

This Python script defines a function `longest` that takes a list of strings as input and returns the longest string. If there are multiple strings of the same length, it returns the first one it encounters. If the input list is empty, it returns `None`. The script also includes test cases to verify that the function behaves as expected.