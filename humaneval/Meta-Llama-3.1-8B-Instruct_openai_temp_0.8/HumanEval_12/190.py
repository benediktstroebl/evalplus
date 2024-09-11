```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    >>> longest([])
    # Output: None

    >>> longest(['a', 'b', 'c'])
    # Output: 'a'

    >>> longest(['a', 'bb', 'ccc'])
    # Output: 'ccc'
    """
    if not strings:  # Check if list is empty
        return None
    longest_str = max(strings, key=len)  # Find the longest string
    return longest_str  # Return the longest string

# Example usage
print(longest([]))  # Output: None
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

This Python script uses the built-in `max` function with the `key` parameter set to `len` to find the longest string in the list. The `if not strings` check ensures that the function returns `None` when the input list is empty.