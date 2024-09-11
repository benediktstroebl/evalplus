```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string, or None if the input list is empty.
    """

    # Check if the input list is empty and return None in this case
    if not strings:
        return None

    # Use the max function with a key argument to find the longest string
    # The key argument specifies that the max function should compare the lengths of the strings
    # The max function returns the first maximum element it encounters, so this meets the requirement
    # of returning the first string in case of multiple strings of the same length
    return max(strings, key=len)


# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```