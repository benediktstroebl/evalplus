```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from a list of strings. If multiple strings have the same maximum length,
    returns the first one. If the input list is empty, returns None.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:
        # If the list is empty, return None
        return None
    
    # Use the max function with a key function to find the longest string
    # The key function is a lambda function that returns the length of a string
    # The max function will return the first string with the maximum length
    return max(strings, key=lambda s: len(s))

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```