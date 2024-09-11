```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: A list of strings
    :return: The longest string in the list, or None if the list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)


# Test cases
assert longest([]) is None
assert longest(['a', 'b', 'c']) == 'a'
assert longest(['a', 'bb', 'ccc']) == 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. The `max` function is used with the `key` argument set to `len` to find the longest string. The test cases at the end of the script verify that the function works as expected.