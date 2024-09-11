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

    Examples:
        >>> longest([])
        None
        >>> longest(['a', 'b', 'c'])
        'a'
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string in the list


# Test cases
print(longest([])) 
print(longest(['a', 'b', 'c']))
print(longest(['a', 'bb', 'ccc']))
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. The function uses the built-in `max` function with the `key` argument set to `len` to find the longest string. The test cases at the end demonstrate the function's behavior.