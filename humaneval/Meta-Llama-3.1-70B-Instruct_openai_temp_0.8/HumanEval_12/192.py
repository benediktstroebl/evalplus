```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:  # check if the list is empty
        return None
    return max(strings, key=len)  # return the longest string


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. If there are multiple strings with the same maximum length, it returns the first one. The `max` function with the `key` argument is used to find the longest string. The `key` argument specifies a function of one argument that is used to extract a comparison key from each input element. In this case, the `len` function is used to extract the length of each string.