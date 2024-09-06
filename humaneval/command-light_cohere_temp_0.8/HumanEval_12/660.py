```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list.

    If list is empty, return None
    """
    if not strings:
        return None
    # Initialize a variable to store the length of the longest string
    max_length = 0
    # Compare the length of each string in the list
    for string in strings:
        # Update the max_length if the current string is longer
        if len(string) > max_length:
            max_length = len(string)
    # Return the longest string
    return strings[max_length - 1]

# Test cases
print(longest(['a', 'b', 'c']))   # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))          # Output: None
```
The provided solution uses the **typing** module to improve code clarity and maintainability. The function **longest** takes a list of strings as input and returns the longest string in the list.