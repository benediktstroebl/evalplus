```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        # If the list is empty, return None
        return None
    
    # Use the max function with a key argument to find the longest string
    # The key argument specifies that the max function should compare the lengths of the strings
    # The max function will return the first string with the maximum length in case of a tie
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print None
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```