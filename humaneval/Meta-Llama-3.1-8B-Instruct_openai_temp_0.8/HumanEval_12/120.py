```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    # Check if the list is empty
    if not strings:
        return None
    
    # Return the first string in the list because Python's built-in max function
    # returns the first item in case of a tie
    return max(strings, key=len)

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. Otherwise, it uses the `max` function with the `key` argument set to `len` to find the longest string. The `max` function returns the first item in case of a tie, which is why we get the first string in case of multiple strings of the same length. The script also includes test cases to verify that the function works correctly.