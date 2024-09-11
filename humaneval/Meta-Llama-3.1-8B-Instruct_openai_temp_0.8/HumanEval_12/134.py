```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Args:
    strings (List[str]): A list of strings

    Returns:
    Optional[str]: The longest string in the list. If the list is empty, return None.
    """
    # Check if the list is empty, return None if it is
    if not strings:
        return None
    
    # Initialize the longest string with the first string in the list
    longest_str = strings[0]
    
    # Iterate over each string in the list
    for s in strings:
        # If the current string is longer than the longest string found so far, update longest string
        if len(s) > len(longest_str):
            longest_str = s
    
    # Return the longest string found
    return longest_str

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This Python script defines a function `longest` which takes a list of strings as input and returns the longest string in the list. In case of multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`. The script includes test cases to demonstrate its correctness.