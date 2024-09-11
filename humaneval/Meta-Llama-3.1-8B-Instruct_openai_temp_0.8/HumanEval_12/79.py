```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
    - strings (List[str]): A list of strings

    Returns:
    - Optional[str]: The longest string in the list, or None if the list is empty
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string using the max function with key=len

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The `key` argument is used to specify a function of one argument that is used to extract a comparison key from each element in the iterable. In this case, `len` is used as the comparison key, so the `max` function returns the longest string in the list. If the input list is empty, the `max` function returns `None`, and we bail out of the function early with the `if not strings` check.