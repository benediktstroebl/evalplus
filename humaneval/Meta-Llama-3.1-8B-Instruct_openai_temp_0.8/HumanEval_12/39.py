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
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # check if the list is empty
        return None
    longest_str = strings[0]  # initialize the longest string as the first one in the list
    for s in strings:  # iterate over the list
        if len(s) > len(longest_str):  # check if the current string is longer
            longest_str = s  # update the longest string
    return longest_str  # return the longest string


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the list is empty, it returns `None`. The function uses a simple iterative approach to find the longest string, starting with the first string in the list and updating the longest string whenever a longer string is found. The test cases at the end verify the correctness of the function.