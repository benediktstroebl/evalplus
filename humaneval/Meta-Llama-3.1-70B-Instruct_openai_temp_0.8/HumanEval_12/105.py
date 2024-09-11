```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None  # Return None if the list is empty

    longest_str = max(strings, key=len)  # Use max() with key=len to find the longest string
    return longest_str  # Return the longest string


# Test cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, the function returns `None`. The `max` function with `key=len` is used to find the longest string in the list. The script also includes test cases to verify the correctness of the function.