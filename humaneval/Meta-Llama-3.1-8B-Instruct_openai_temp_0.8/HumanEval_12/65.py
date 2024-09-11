### Longest String in a List
#### Problem Description
Given a list of strings, return the longest string. If there are multiple strings of the same length, return the first one. If the input list is empty, return None.

#### Solution
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
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    # Check if the list is empty
    if not strings:
        return None

    # Use max with a key to find the longest string
    # max will return the first string in case of a tie
    return max(strings, key=len)

# Example use cases
print(longest([]))  # Output: None

print(longest(['a', 'b', 'c']))  # Output: 'a'

print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```

This solution uses the built-in `max` function with the `key` argument set to `len`, which returns the length of each string. This tells `max` to find the string with the maximum length. If multiple strings have the same maximum length, `max` will return the first one it encounters, which matches the problem description.