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
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    max_length = 0  # Initialize max_length to 0
    longest_str = ""  # Initialize longest_str to an empty string
    for string in strings:
        if len(string) > max_length:  # Check if the current string is longer than max_length
            max_length = len(string)  # Update max_length
            longest_str = string  # Update longest_str
    return longest_str  # Return the longest string

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines the `longest` function which takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. If there are multiple strings of the same maximum length, it returns the first one encountered. The script includes test cases to verify its correctness.