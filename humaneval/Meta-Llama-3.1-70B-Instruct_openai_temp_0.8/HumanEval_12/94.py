```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the list is empty.
    """
    if not strings:  # check if the list is empty
        return None

    # use max function with key argument to find the longest string
    # in case of multiple strings with the same length, max returns the first one
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings and returns the longest string. If there are multiple strings with the same maximum length, it returns the first one. If the input list is empty, it returns `None`.

The function uses the built-in `max` function with the `key` argument set to `len` to find the longest string. The `max` function returns the first item with the maximum value, so in case of multiple strings with the same length, it returns the first one.

The script also includes test cases to demonstrate the function's behavior.