```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script uses Python's built-in `max` function with the `key` argument to find the longest string in the list. The `key` argument specifies a function of one argument that is used to extract a comparison key from each input element. In this case, the `len` function is used to compare the lengths of the strings. If the input list is empty, the function returns `None`.