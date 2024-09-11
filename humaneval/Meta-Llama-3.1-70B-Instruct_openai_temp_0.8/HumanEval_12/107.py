```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the list is empty.
    """
    if not strings:
        # If the list is empty, return None
        return None
    else:
        # Use the built-in max function with key=len to find the longest string
        # The max function returns the first item with the maximum value in case of multiple items with the same maximum value
        return max(strings, key=len)


# Test cases
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```