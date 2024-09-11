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
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. The `max` function with `key=len` is used to find the longest string. If the input list is empty, the function returns `None`. The test cases are included to demonstrate the function's behavior with different inputs.