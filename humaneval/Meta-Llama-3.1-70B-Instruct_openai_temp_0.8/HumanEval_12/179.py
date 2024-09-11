```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty
    """
    if not strings:  # check if the list is empty
        return None

    # use the max function with a key argument to find the longest string
    # the key argument specifies that we want to use the length of the string as the comparison key
    return max(strings, key=len)


# test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines the function `longest` that takes a list of strings as an argument and returns the longest string. If the input list is empty, it returns `None`. If there are multiple strings of the same length, it returns the first one. The `max` function is used with a key argument to find the longest string. The `key` argument specifies that we want to use the length of the string as the comparison key.