```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:
        return None  # Return None for an empty list
    return max(strings, key=len)  # Return the longest string


# Test cases
print(longest([]))  # Should print: None

print(longest(['a', 'b', 'c']))  # Should print: 'a'

print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

In this script, the `longest` function uses the built-in `max` function with the `key` argument set to `len` to find the longest string in the input list. If the list is empty, it returns `None`. The test cases are included to verify that the function works as expected.