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
    if not strings:  # check if list is empty
        return None
    return max(strings, key=len)  # return the longest string

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

In this script, we first check if the list is empty. If it is, we return None as per the problem statement. If the list is not empty, we use the built-in `max` function along with the `key` argument to find the longest string in the list. The `key` argument specifies a function of one argument that is used to extract a comparison key from each element in the list. In this case, the function `len` is used to extract the length of each string, so `max` will return the string with the maximum length. If there are multiple strings of the same maximum length, `max` will return the first one it encounters, as specified in the problem statement.