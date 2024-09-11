```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:  # Check if the input list is empty
        return None
    return max(strings, key=len)  # Return the longest string using the max function with len as key

# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```