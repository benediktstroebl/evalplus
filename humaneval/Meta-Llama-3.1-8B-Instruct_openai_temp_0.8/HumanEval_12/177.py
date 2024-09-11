```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    
    Args:
    strings (List[str]): A list of strings
    
    Returns:
    Optional[str]: The longest string in the list or None if the list is empty
    
    Examples:
    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:  # Check if the list is empty
        return None
    else:
        return max(strings, key=len)  # Return the longest string

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

In this script, we use the built-in Python function `max()` with the `key` argument set to `len` to find the longest string in the list. If the list is empty, we return `None`.