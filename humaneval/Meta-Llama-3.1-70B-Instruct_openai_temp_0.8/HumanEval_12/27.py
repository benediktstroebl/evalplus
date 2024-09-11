```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string from the input list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    
    # Use the max function with the key argument to find the longest string
    # The max function returns the first maximum element in case of multiple maxima
    return max(strings, key=len)


# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```