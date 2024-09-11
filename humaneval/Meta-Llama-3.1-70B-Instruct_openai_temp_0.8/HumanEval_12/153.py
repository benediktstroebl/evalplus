```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string, or None if the list is empty
    """
    if not strings:
        # If the list is empty, return None
        return None
    else:
        # Use the max function with a key function to find the longest string
        # The key function returns the length of each string
        # The max function returns the first maximum element it finds
        return max(strings, key=len)


# Test cases
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```