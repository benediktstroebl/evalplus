```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # check if the list is empty
        return None

    # use the max function with a custom key to find the longest string
    # the key function returns the length of each string
    # the max function will return the first item with the maximum length
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. If there are multiple strings with the same maximum length, it returns the first one. The function uses the built-in `max` function with a custom key to find the longest string. The key function returns the length of each string, and the `max` function returns the first item with the maximum length. The script also includes test cases to verify the function's behavior.