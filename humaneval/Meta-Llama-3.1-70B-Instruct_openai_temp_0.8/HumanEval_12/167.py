```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    """
    
    # Check if the input list is empty
    if not strings:
        # If it is, return None
        return None

    # Use the built-in max function with a key function that returns the length of a string
    # This will return the first string with the maximum length
    return max(strings, key=len)

# Test the function
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If there are multiple strings with the same maximum length, it returns the first one. If the input list is empty, it returns `None`. The function uses the built-in `max` function with a `key` function that returns the length of a string to find the longest string. The script also includes some test cases to demonstrate the function's behavior.