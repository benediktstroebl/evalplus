```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty
    """
    # Check if the input list is empty
    if not strings:
        return None
    
    # Use the max function with a key argument to find the longest string
    # The key argument tells max to compare strings based on their length
    return max(strings, key=len)

# Test cases
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'

print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines the `longest` function as specified, and includes test cases to verify that it works correctly. The `max` function is used with a key of `len` to find the longest string in the list. If the input list is empty, the function returns `None`.