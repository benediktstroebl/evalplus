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
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize longest_str as the first string in the list
    max_length = len(longest_str)  # Initialize max_length as the length of the first string

    for string in strings:
        if len(string) > max_length:  # If a string is longer than max_length
            longest_str = string  # Update longest_str with the current string
            max_length = len(string)  # Update max_length with the length of the current string

    return longest_str  # Return the longest string

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. If there are multiple strings of the same length, it returns the first one encountered. The test cases at the end of the script verify the correctness of the function.