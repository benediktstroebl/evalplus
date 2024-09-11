```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None

    # Use the max function with a custom key to find the longest string
    # The key is a lambda function that returns the length of a string
    # The max function will return the first string with the maximum length
    return max(strings, key=lambda s: len(s))


# Test cases
print(longest([]))  # Should not print anything
print(longest(['a', 'b', 'c']))  # Should print 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print 'ccc'
```